# Backend README artwork

Original artwork created for the Backend landing page: request packets, an API server, a database, a cache, a background worker, and a terminal learning loop.

| File | Use |
| --- | --- |
| `backend-hero.gif` | Animated opening banner, 1200 × 440 |
| `backend-footer.gif` | Animated terminal footer, 1200 × 190 |
| `backend-hero.svg` | Static opening banner for reduced motion |
| `backend-footer.svg` | Static footer for reduced motion |
| `backend-divider.svg` | Full-width circuit divider with a large code symbol, 1200 × 112 |

The README uses relative image paths. Keep these files in `Backend/assets/` alongside the README at `Backend/README.md`.

## Regenerate the artwork

The source of the artwork is `generate_assets.py`. It uses vector shapes and local DejaVu fonts; it does not download images or reuse the repository's CIS artwork.

```bash
python -m pip install Pillow PyMuPDF
python Backend/assets/generate_assets.py
```

Run the script in an environment with DejaVu Sans and DejaVu Sans Mono installed under `/usr/share/fonts/truetype/dejavu/`, or update the font paths in the script for your operating system. The script writes the GIF and SVG assets to this directory and prints the location of temporary PNG previews.

The animation illustrates possible backend components. It is not a requirement to add every component to every project.
