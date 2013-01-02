# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.38
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        try:
            fp, pathname, description = imp.find_module('_flysky_swig', [dirname(__file__)])
            _mod = imp.load_module('_flysky_swig', fp, pathname, description)
        finally:
            if fp is not None: fp.close()
        return _mod
    _flysky_swig = swig_import_helper()
    del swig_import_helper
else:
    import _flysky_swig
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class SwigPyIterator(object):
    """Proxy of C++ swig::SwigPyIterator class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _flysky_swig.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self):
        """value(self) -> PyObject"""
        return _flysky_swig.SwigPyIterator_value(self)

    def incr(self, n = 1):
        """incr(self, size_t n = 1) -> SwigPyIterator"""
        return _flysky_swig.SwigPyIterator_incr(self, n)

    def decr(self, n = 1):
        """decr(self, size_t n = 1) -> SwigPyIterator"""
        return _flysky_swig.SwigPyIterator_decr(self, n)

    def distance(self, *args, **kwargs):
        """distance(self, SwigPyIterator x) -> ptrdiff_t"""
        return _flysky_swig.SwigPyIterator_distance(self, *args, **kwargs)

    def equal(self, *args, **kwargs):
        """equal(self, SwigPyIterator x) -> bool"""
        return _flysky_swig.SwigPyIterator_equal(self, *args, **kwargs)

    def copy(self):
        """copy(self) -> SwigPyIterator"""
        return _flysky_swig.SwigPyIterator_copy(self)

    def next(self):
        """next(self) -> PyObject"""
        return _flysky_swig.SwigPyIterator_next(self)

    def __next__(self):
        """__next__(self) -> PyObject"""
        return _flysky_swig.SwigPyIterator___next__(self)

    def previous(self):
        """previous(self) -> PyObject"""
        return _flysky_swig.SwigPyIterator_previous(self)

    def advance(self, *args, **kwargs):
        """advance(self, ptrdiff_t n) -> SwigPyIterator"""
        return _flysky_swig.SwigPyIterator_advance(self, *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        """__eq__(self, SwigPyIterator x) -> bool"""
        return _flysky_swig.SwigPyIterator___eq__(self, *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        """__ne__(self, SwigPyIterator x) -> bool"""
        return _flysky_swig.SwigPyIterator___ne__(self, *args, **kwargs)

    def __iadd__(self, *args, **kwargs):
        """__iadd__(self, ptrdiff_t n) -> SwigPyIterator"""
        return _flysky_swig.SwigPyIterator___iadd__(self, *args, **kwargs)

    def __isub__(self, *args, **kwargs):
        """__isub__(self, ptrdiff_t n) -> SwigPyIterator"""
        return _flysky_swig.SwigPyIterator___isub__(self, *args, **kwargs)

    def __add__(self, *args, **kwargs):
        """__add__(self, ptrdiff_t n) -> SwigPyIterator"""
        return _flysky_swig.SwigPyIterator___add__(self, *args, **kwargs)

    def __sub__(self, *args):
        """
        __sub__(self, ptrdiff_t n) -> SwigPyIterator
        __sub__(self, SwigPyIterator x) -> ptrdiff_t
        """
        return _flysky_swig.SwigPyIterator___sub__(self, *args)

    def __iter__(self): return self
SwigPyIterator_swigregister = _flysky_swig.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class flysky_dumpsync_sptr(object):
    """Proxy of C++ boost::shared_ptr<(flysky_dumpsync)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> flysky_dumpsync_sptr
        __init__(self,  p) -> flysky_dumpsync_sptr
        """
        this = _flysky_swig.new_flysky_dumpsync_sptr(*args)
        try: self.this.append(this)
        except: self.this = this
    def __deref__(self):
        """__deref__(self)"""
        return _flysky_swig.flysky_dumpsync_sptr___deref__(self)

    __swig_destroy__ = _flysky_swig.delete_flysky_dumpsync_sptr
    __del__ = lambda self : None;
    def work(self, *args, **kwargs):
        """
        work(self, int noutput_items, gr_vector_const_void_star input_items, 
            gr_vector_void_star output_items) -> int

        Params: (noutput_items, input_items, output_items)
        """
        return _flysky_swig.flysky_dumpsync_sptr_work(self, *args, **kwargs)

    def history(self):
        """history(self) -> unsigned int"""
        return _flysky_swig.flysky_dumpsync_sptr_history(self)

    def output_multiple(self):
        """output_multiple(self) -> int"""
        return _flysky_swig.flysky_dumpsync_sptr_output_multiple(self)

    def relative_rate(self):
        """relative_rate(self) -> double"""
        return _flysky_swig.flysky_dumpsync_sptr_relative_rate(self)

    def start(self):
        """start(self) -> bool"""
        return _flysky_swig.flysky_dumpsync_sptr_start(self)

    def stop(self):
        """stop(self) -> bool"""
        return _flysky_swig.flysky_dumpsync_sptr_stop(self)

    def nitems_read(self, *args, **kwargs):
        """nitems_read(self, unsigned int which_input) -> uint64_t"""
        return _flysky_swig.flysky_dumpsync_sptr_nitems_read(self, *args, **kwargs)

    def nitems_written(self, *args, **kwargs):
        """nitems_written(self, unsigned int which_output) -> uint64_t"""
        return _flysky_swig.flysky_dumpsync_sptr_nitems_written(self, *args, **kwargs)

    def detail(self):
        """detail(self) -> gr_block_detail_sptr"""
        return _flysky_swig.flysky_dumpsync_sptr_detail(self)

    def set_detail(self, *args, **kwargs):
        """set_detail(self, gr_block_detail_sptr detail)"""
        return _flysky_swig.flysky_dumpsync_sptr_set_detail(self, *args, **kwargs)

    def name(self):
        """name(self) -> string"""
        return _flysky_swig.flysky_dumpsync_sptr_name(self)

    def input_signature(self):
        """input_signature(self) -> gr_io_signature_sptr"""
        return _flysky_swig.flysky_dumpsync_sptr_input_signature(self)

    def output_signature(self):
        """output_signature(self) -> gr_io_signature_sptr"""
        return _flysky_swig.flysky_dumpsync_sptr_output_signature(self)

    def unique_id(self):
        """unique_id(self) -> long"""
        return _flysky_swig.flysky_dumpsync_sptr_unique_id(self)

    def to_basic_block(self):
        """to_basic_block(self) -> gr_basic_block_sptr"""
        return _flysky_swig.flysky_dumpsync_sptr_to_basic_block(self)

    def check_topology(self, *args, **kwargs):
        """check_topology(self, int ninputs, int noutputs) -> bool"""
        return _flysky_swig.flysky_dumpsync_sptr_check_topology(self, *args, **kwargs)

flysky_dumpsync_sptr_swigregister = _flysky_swig.flysky_dumpsync_sptr_swigregister
flysky_dumpsync_sptr_swigregister(flysky_dumpsync_sptr)

flysky_dumpsync_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id ())


def dumpsync():
  """
    dumpsync() -> flysky_dumpsync_sptr

    <+description+>

    Params: (NONE)
    """
  return _flysky_swig.dumpsync()
class flysky_bind_code_sptr(object):
    """Proxy of C++ boost::shared_ptr<(flysky_bind_code)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> flysky_bind_code_sptr
        __init__(self,  p) -> flysky_bind_code_sptr
        """
        this = _flysky_swig.new_flysky_bind_code_sptr(*args)
        try: self.this.append(this)
        except: self.this = this
    def __deref__(self):
        """__deref__(self)"""
        return _flysky_swig.flysky_bind_code_sptr___deref__(self)

    __swig_destroy__ = _flysky_swig.delete_flysky_bind_code_sptr
    __del__ = lambda self : None;
    def work(self, *args, **kwargs):
        """
        work(self, int noutput_items, gr_vector_const_void_star input_items, 
            gr_vector_void_star output_items) -> int

        Params: (noutput_items, input_items, output_items)
        """
        return _flysky_swig.flysky_bind_code_sptr_work(self, *args, **kwargs)

    def history(self):
        """history(self) -> unsigned int"""
        return _flysky_swig.flysky_bind_code_sptr_history(self)

    def output_multiple(self):
        """output_multiple(self) -> int"""
        return _flysky_swig.flysky_bind_code_sptr_output_multiple(self)

    def relative_rate(self):
        """relative_rate(self) -> double"""
        return _flysky_swig.flysky_bind_code_sptr_relative_rate(self)

    def start(self):
        """start(self) -> bool"""
        return _flysky_swig.flysky_bind_code_sptr_start(self)

    def stop(self):
        """stop(self) -> bool"""
        return _flysky_swig.flysky_bind_code_sptr_stop(self)

    def nitems_read(self, *args, **kwargs):
        """nitems_read(self, unsigned int which_input) -> uint64_t"""
        return _flysky_swig.flysky_bind_code_sptr_nitems_read(self, *args, **kwargs)

    def nitems_written(self, *args, **kwargs):
        """nitems_written(self, unsigned int which_output) -> uint64_t"""
        return _flysky_swig.flysky_bind_code_sptr_nitems_written(self, *args, **kwargs)

    def detail(self):
        """detail(self) -> gr_block_detail_sptr"""
        return _flysky_swig.flysky_bind_code_sptr_detail(self)

    def set_detail(self, *args, **kwargs):
        """set_detail(self, gr_block_detail_sptr detail)"""
        return _flysky_swig.flysky_bind_code_sptr_set_detail(self, *args, **kwargs)

    def name(self):
        """name(self) -> string"""
        return _flysky_swig.flysky_bind_code_sptr_name(self)

    def input_signature(self):
        """input_signature(self) -> gr_io_signature_sptr"""
        return _flysky_swig.flysky_bind_code_sptr_input_signature(self)

    def output_signature(self):
        """output_signature(self) -> gr_io_signature_sptr"""
        return _flysky_swig.flysky_bind_code_sptr_output_signature(self)

    def unique_id(self):
        """unique_id(self) -> long"""
        return _flysky_swig.flysky_bind_code_sptr_unique_id(self)

    def to_basic_block(self):
        """to_basic_block(self) -> gr_basic_block_sptr"""
        return _flysky_swig.flysky_bind_code_sptr_to_basic_block(self)

    def check_topology(self, *args, **kwargs):
        """check_topology(self, int ninputs, int noutputs) -> bool"""
        return _flysky_swig.flysky_bind_code_sptr_check_topology(self, *args, **kwargs)

flysky_bind_code_sptr_swigregister = _flysky_swig.flysky_bind_code_sptr_swigregister
flysky_bind_code_sptr_swigregister(flysky_bind_code_sptr)

flysky_bind_code_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id ())


def bind_code(*args, **kwargs):
  """
    bind_code(int bind_code) -> flysky_bind_code_sptr

    <+description+>

    Params: (bind_code)
    """
  return _flysky_swig.bind_code(*args, **kwargs)


