# Hide Silkscreen References
A simple KiCad plugin to hide reference designators on the silkscreen layer.
It uses the default reference field, with an option to skip locked components, and toggles visibility accordingly.

## Installation
Copy or link this directory into your KiCad plugins folder.
Then restart KiCad or reload the plugins — the plugin should appear in the Tools → External Plugins dropdown.

For more on installing plugins, see the [KiCad Plugin Documentation](https://docs.kicad.org/8.0/en/pcbnew/pcbnew.html#action_plugins) and the [KiCad Plugins Framework](https://dev-docs.kicad.org/en/components/plugins/).

## Explanation
I wrote a blog post [here](https://maskset.net/kicad-pcbnew-scripting-removing-ref-des-from-silk-screen.html) that explains the approach in detail, including scripting and visibility toggling.

## Notes
Turn out KiCad also offers a manual way to do this via Edit → Edit Text and Graphic Properties, which can hide references by layer or field.
