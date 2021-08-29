from npe2 import register_command


def activate(context):
    @register_command("my_plugin.hello_world")
    def _hello():
        from napari.utils.notifications import show_info

        show_info("Hello World!")

    register_command("my_plugin.another_command", lambda: print("yo!"))
