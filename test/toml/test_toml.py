from tomlkit import TOMLDocument

from mktech.toml import merge


def test_merge() -> None:
    document = TOMLDocument()

    document.update(
        {
            'log_level': 'WARNING',
            'modules': [],
            'zsh': {'fzf': False, 'lsd': False},
            'ssh': {'use_ssh': False, 'port': 22}
        }
    )

    new_doc = merge(
        document,
        {'log_level': 'INFO', 'new_key': 'new_val', 'zsh': {'fzf': True}}
    )

    assert dict(new_doc) == {
        'log_level': 'INFO',
        'new_key': 'new_val',
        'modules': [],
        'zsh': {'fzf': True, 'lsd': False},
        'ssh': {'use_ssh': False, 'port': 22}
    }
