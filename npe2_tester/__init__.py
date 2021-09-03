try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"


def activate(context):
    from npe2 import register_command

    # one way to do it
    @register_command("my_plugin.hello_world")
    def _hello():
        from napari.utils.notifications import show_info

        show_info("Hello World!")

    # another way to do it
    register_command("my_plugin.another_command", lambda: print("yo!"))


# this is an example of a function that is registered directly
# via python_name in the manifest
def get_reader(path):
    def reader(path):
        import tifffile

        return [(tifffile.imread(path),)]
