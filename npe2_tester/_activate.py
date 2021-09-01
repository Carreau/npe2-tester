def reader(path):
    import tifffile

    return [(tifffile.imread(path),)]


def activate(context):
    from npe2 import register_command

    # one way to do it
    @register_command("my_plugin.hello_world")
    def _hello():
        from napari.utils.notifications import show_info

        show_info("Hello World!")

    # another way to do it
    register_command("my_plugin.another_command", lambda: print("yo!"))
    register_command("my_plugin.my_reader", lambda path: reader)
