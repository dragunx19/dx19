-- Change the default Omarchy look'n'feel to Windows 11 style.

-- https://wiki.hypr.land/Configuring/Basics/Variables/#general
hl.config({
  general = {
    -- No gaps between windows or borders.
    gaps_in = 0,
    gaps_out = 0,
    border_size = 1,

    -- Change to niri-like side-scrolling layout.
    layout = "scrolling",
  },
})

-- https://wiki.hypr.land/Configuring/Basics/Variables/#decoration
hl.config({
  decoration = {
    -- Use round window corners.
    rounding = 8,

    -- Dim unfocused windows (0.0 = no dim, 1.0 = fully dimmed).
    dim_inactive = true,
    dim_strength = 0.15,
    
    -- Add transparent background with blur effect
    blur = {
      enabled = true,
      size = 3,
      passes = 1,
      vibrancy = 0.05,
      ignore_opacity = true
    },
  },
})

-- https://wiki.hypr.land/Configuring/Basics/Variables/#animations
hl.config({
  animations = {
    -- Enable animations for smoother experience.
    enabled = true,
    -- Animation duration in ms.
    bezier = "default",
    animation = {
      duration = 0.2,
      ease = "linear",
    }
  },
})

-- https://wiki.hypr.land/Configuring/Basics/Variables/#layout
hl.config({
  layout = {
    -- Avoid overly wide single-window layouts on wide screens.
    single_window_aspect_ratio = { 1, 1 },
  },
})

-- https://wiki.hypr.land/Configuring/Layouts/Scrolling-Layout/
hl.config({
  scrolling = {
    -- See only one column per screen instead of two.
    column_width = 0.97,
  },
})