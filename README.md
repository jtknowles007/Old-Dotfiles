Dotfiles
==========

My personal repository of dotfiles. I hate having a bunch of different configurations on my various computers, so I did a little research and found this to be the best method (for me, at least) to keep everything synced up.  I love that I can now make configuration changes from any of my computers and push out the changes to the others so quickly and easily!

The method I'm currently using requires the use of [git](https://git-scm.com/) and [GNU stow](https://www.gnu.org/software/stow/).  You can clone my repository for your own use by following these instructions:

```bash
$ git clone https://github.com/jtknowles007/dotfiles.git ~/dotfiles
$ cd ~/dotfiles
$ stow bash vim i3 compton (and anything else I may have added since)
```
These certainly aren't the best configuration files around, but they're what works for me. I've cobbled together a bunch of different tidbits that I've found around the web to come up these files. You can find lots of great information about dotfiles on GitHub at [dotfiles.github.io](http://dotfiles.github.io)  My repository will surely evolve over time. I hope you find something useful!

John K.
