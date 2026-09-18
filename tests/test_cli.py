from kite5.cli import main


def _run(argv, monkeypatch):
    monkeypatch.setattr("sys.argv", ["kite5", *argv])
    main()


def test_cli_mass(capsys, monkeypatch):
    _run(["mass"], monkeypatch)
    out = capsys.readouterr().out
    assert "Kite-5" in out


def test_cli_hover(capsys, monkeypatch):
    _run(["hover", "--thrust-g", "650", "--disk-cm", "12.7"], monkeypatch)
    out = capsys.readouterr().out
    assert "P_induced" in out


def test_cli_mixer(capsys, monkeypatch):
    _run(["mixer", "--throttle", "0.5", "--roll", "0.2"], monkeypatch)
    out = capsys.readouterr().out
    assert "m1:" in out and "m4:" in out
