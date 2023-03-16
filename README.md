# nvim-kitty-navigator

Navigate seamlessly between Kitty and Neovim windows.

This [kitten](https://sw.kovidgoyal.net/kitty/kittens/custom/) is inspired by
[vim-tmux-navigator](https://github.com/christoomey/vim-tmux-navigator) and
[vim-kitty-navigator](https://github.com/knubie/vim-kitty-navigator).

Unlike its inspirations, nvim-kitty-navigator doesn't require a Neovim plugin.
Instead, [pynvim](https://github.com/neovim/pynvim) is used to control Neovim
programatically.

## Installation

This script requires `pynvim`:

```bash
pip install pynvim
```

Then download the kitten to `~/.config/kitty/`.

```bash
curl https://raw.githubusercontent.com/ouroboros8/nvim-kitty-navigator/main/navigate.py -o ~/.config/kitty/navigate.py
```

## Configuration

Add the following (changing the mappings to whatever you like!) to your `kitty.conf`:

```
map ctrl+h kitten navigate.py left
map ctrl+j kitten navigate.py down
map ctrl+k kitten navigate.py up
map ctrl+l kitten navigate.py right
```

## Notes

The kitten makes a couple of assumptions about your neovim setup:

0. It expects Neovim to create a default RPC socket in its runpath at startup, as described in [the API docs](https://neovim.io/doc/user/api.html#rpc-connecting). Using `--listen` will likely break the kitten!
0. It expects the socket to have a predictable name in the format `nvim.<pid>.<n>`
0. It expects the standard runpath not to change from one vim instance to another, or over the life of a Kitty process. The path is discovered by running `:echo stdpath('run')` on a headless Neovim instance, then cached until Kitty exits.

If any of these assumptions cause you issues, feel free to raise an issue!
