import pygame


def load_sprite(path, size=None, scale=None, rotate=0):
    """Load an image as a display-ready, anti-aliased surface.

    - convert_alpha() gives correct per-pixel alpha and fast blits.
    - rotate is applied first (use exact multiples of 90 for lossless results).
    - smoothscale gives anti-aliased resizing; pass either an explicit ``size``
      (width, height) or a uniform ``scale`` factor.
    """
    image = pygame.image.load(path).convert_alpha()
    if rotate:
        image = pygame.transform.rotate(image, rotate)
    if size is None and scale is not None:
        w, h = image.get_size()
        size = (round(w * scale), round(h * scale))
    if size is not None:
        image = pygame.transform.smoothscale(image, size)
    return image


def make_laser(width, height, color=(80, 180, 255)):
    """Draw a crisp, anti-aliased glowing laser bolt on a transparent surface."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    cx = width / 2
    r = width / 2
    # Soft outer glow: capsules shrinking inward with rising alpha (widest = faintest).
    for pad, alpha in ((0, 70), (1, 120), (2, 190)):
        glow = (color[0], color[1], color[2], alpha)
        pygame.draw.line(surface, glow, (cx, r + pad), (cx, height - r - pad),
                         max(1, int(width - 2 * pad)))
    # Bright core down the middle.
    pygame.draw.line(surface, (255, 255, 255), (cx, r), (cx, height - r),
                     max(1, int(width * 0.4)))
    return surface


def mask_from(image):
    """Pixel-perfect collision mask for a sprite surface."""
    return pygame.mask.from_surface(image)


def masks_collide(a, b):
    """Pixel-perfect collision: rect broad-phase, then mask overlap."""
    if not a.rect.colliderect(b.rect):
        return False
    offset = (b.rect.x - a.rect.x, b.rect.y - a.rect.y)
    return a.mask.overlap(b.mask, offset) is not None
