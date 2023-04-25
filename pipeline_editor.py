def main():
    import argparse
    import sys
    from pathlib import Path

    from Qt import QtWidgets

    from DAINodes import DAINodeGraph
    from NodeGraphQt import setup_context_menu

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        type=Path,
        default=Path(__file__).parent,
        help="Path to save/load default directory",
    )
    parser.add_argument(
        "-o", "--open", type=Path, default=None, help="Path to project file to open"
    )
    args = parser.parse_args()

    app = QtWidgets.QApplication(sys.argv)

    # create node graph controller.
    graph = DAINodeGraph()

    # set up default menu and commands.
    setup_context_menu(graph, set_default_file_path=str(args.path), open_file=args.open)

    # show the node graph widget.
    graph_widget = graph.widget
    graph_widget.show()

    app.exec_()


if __name__ == "__main__":
    main()
