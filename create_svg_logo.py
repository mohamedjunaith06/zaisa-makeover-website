import xml.etree.ElementTree as ET

# We will create an ultra-precise, crystal clear, luxury SVG logo for Zaisa Makeover
# Colors:
# Gold: #b88a44 / #caa058
# Wine/Burgundy: #7a233b / #6a1b30

svg_data = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 480" width="100%" height="100%">
  <defs>
    <!-- Warm Gold Gradient for Crown & Silhouette -->
    <linearGradient id="luxeGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c59b58" />
      <stop offset="50%" stop-color="#af823f" />
      <stop offset="100%" stop-color="#996e30" />
    </linearGradient>

    <!-- Deep Royal Wine Gradient for Typography -->
    <linearGradient id="luxeWine" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7d243c" />
      <stop offset="100%" stop-color="#60162a" />
    </linearGradient>
  </defs>

  <g transform="translate(35, 10)">
    <!-- 1. CROWN (Above Z) -->
    <!-- Center of Z is at x = 115 -->
    <g transform="translate(86, 112) scale(0.68)" fill="url(#luxeGold)">
      <!-- Left pearl -->
      <circle cx="15" cy="18" r="4.8" />
      <!-- Middle pearl -->
      <circle cx="48" cy="8" r="5.6" />
      <!-- Right pearl -->
      <circle cx="81" cy="18" r="4.8" />
      <!-- Crown Body -->
      <path d="M 15 22.5 
               C 22 46, 25 54, 23 57 
               L 73 57 
               C 71 54, 74 46, 81 22.5 
               C 66 38, 57 37, 48 13.5 
               C 39 37, 30 38, 15 22.5 Z" />
      <!-- Base bar -->
      <rect x="20" y="59" width="56" height="4.5" rx="2" />
    </g>

    <!-- 2. WOMAN HEAD PROFILE WITH ELEGANT UPDO BUN (Above I, center at x = 315) -->
    <g transform="translate(268, 25) scale(0.95)" fill="url(#luxeGold)">
      <!-- Bun on top left of head -->
      <path d="M 32 35 C 22 24, 10 26, 4 37 C -2 48, 1 60, 11 67 C 22 74, 33 65, 34 54 C 34 46, 33 40, 32 35 Z" />
      <path d="M 12 36 C 18 28, 28 31, 33 39 C 35 44, 34 51, 29 56 C 23 60, 14 56, 11 49 C 9 44, 10 39, 12 36 Z" fill="#ffffff" opacity="0.35" />

      <!-- Sweeping hair lines & head contour -->
      <!-- Hair strand 1 (top crown) -->
      <path d="M 33 38 C 45 22, 68 25, 78 37 C 86 47, 88 56, 80 61 C 72 65, 60 52, 48 46 C 39 41, 33 39, 33 38 Z" />

      <!-- Hair strand 2 (middle wave) -->
      <path d="M 22 55 C 33 48, 51 48, 64 59 C 74 68, 75 78, 66 80 C 55 82, 43 72, 30 68 C 23 66, 21 59, 22 55 Z" />

      <!-- Hair strand 3 (lower wave) -->
      <path d="M 26 69 C 37 64, 55 66, 62 79 C 66 87, 62 96, 53 100 C 44 104, 35 94, 28 85 C 24 79, 24 74, 26 69 Z" />

      <!-- Profile of Face & graceful flowing lock going down to 'I' -->
      <path d="M 78 37 
               C 83 44, 88 53, 88 60 
               C 85 62, 83 63, 81 64 
               C 85 68, 89 73, 94 77 
               C 92 80, 86 82, 83 83 
               C 86 86, 88 88, 85 91 
               C 82 93, 77 93, 75 94 
               C 77 98, 77 101, 73 103 
               C 67 107, 60 107, 56 110 
               C 49 116, 45 125, 43 138 
               C 41 148, 43 159, 48 171 
               C 42 157, 36 141, 34 125 
               C 32 111, 37 100, 44 91 
               C 51 82, 60 77, 65 68 
               C 67 63, 67 56, 62 51 
               C 57 46, 47 41, 41 41 
               C 53 34, 67 32, 78 37 Z" />
    </g>

    <!-- 3. 'ZAISA' HIGH CONTRAST LUXURY SERIF TYPOGRAPHY -->
    <g fill="url(#luxeWine)">
      <!-- Z -->
      <path d="M 68 180 L 168 180 L 168 195 L 98 274 L 172 274 L 172 291 L 62 291 L 62 276 L 132 197 L 68 197 Z" />

      <!-- A -->
      <path d="M 212 180 L 235 180 L 280 291 L 257 291 L 246 262 L 201 262 L 190 291 L 168 291 Z 
               M 223.5 204 L 207 246 L 240 246 Z" />

      <!-- I (Thick bar centered directly under woman's lock at x = 315) -->
      <path d="M 303 180 L 327 180 L 327 291 L 303 291 Z" />

      <!-- S -->
      <path d="M 416 207 C 411 192, 398 180, 377 180 C 354 180, 341 192, 341 207 C 341 223, 354 232, 374 238 C 401 247, 417 258, 417 275 C 417 294, 399 306, 375 306 C 348 306, 332 293, 327 275 L 348 270 C 352 284, 362 291, 375 291 C 389 291, 397 284, 397 274 C 397 261, 386 252, 366 245 C 341 237, 323 225, 323 207 C 323 188, 341 166, 377 166 C 400 166, 418 179, 423 199 Z" />

      <!-- A -->
      <path d="M 462 180 L 485 180 L 530 291 L 507 291 L 496 262 L 451 262 L 440 291 L 418 291 Z 
               M 473.5 204 L 457 246 L 490 246 Z" />
    </g>

    <!-- 4. 'MAKEOVER' SUBTITLE -->
    <text x="315" y="348" 
          font-family="'Manrope', 'Montserrat', 'Century Gothic', 'Segoe UI', sans-serif" 
          font-size="32" 
          font-weight="600" 
          letter-spacing="10" 
          fill="#7d243c" 
          text-anchor="middle">MAKEOVER</text>
  </g>
</svg>
"""

with open('static/logo.svg', 'w', encoding='utf-8') as f:
    f.write(svg_data)

print("Generated static/logo.svg")
