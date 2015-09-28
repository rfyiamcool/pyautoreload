#coding:utf--8
import imp
import sys
import types
import importlib

#内建函数
_is_builtin = imp.is_builtin

#重载
_reload = reload

#to do
def watch(addr):
    pass

def import_str(objpath):
    objlist = objpath.split('.')
    func = objlist[-1]
    module_path = objlist[:-1]
    obj = __import__(module_path,globals(),locals(),[func])
    return getattr(obj,func)

def delete_module(obj):
    if isinstance(obj,types.ModuleType):
        del obj
        return True
    return False

def delete_str(objpath):
    objlist = objpath.split('.')
    func = objlist[-1]
    module_path = objlist[:-1]
    del sys.modules[module_path]

def reload_str(obj):
    delete_str(obj)
    import_str(obj)

def _get_dependencies(module):
    for variable in vars(module).values():
        if not isinstance(variable, types.ModuleType):
            continue
        if _is_builtin(variable.__name__):
            continue
        yield variable

def _get_modules_in_order(module, done=set()):
    done = {module.__name__}
    for dependency in _get_dependencies(module):
        if dependency.__name__ not in done:
            for subdependency in _get_modules_in_order(dependency, done):
                yield subdependency
    yield module

def reload_module(module):
    for module in _get_modules_in_order(module):
        if module.__name__ in sys.modules:
            try:
                sys.modules[module.__name__] = _reload(module)
            except ImportError:
                continue

def reload_all():
    """
    重新加载所有模块
    """
    for name, module in sys.modules.items():
        if module and name != '__main__':
            reload_module(module)
