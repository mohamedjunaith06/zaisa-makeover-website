import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont
import os

# We will create static/logo.svg and static/logo.png with high resolution and crisp transparency
# First let's craft a beautiful, precise SVG

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 450" width="100%" height="100%">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d4af6d" />
      <stop offset="50%" stop-color="#b88944" />
      <stop offset="100%" stop-color="#9a6e30" />
    </linearGradient>
    <linearGradient id="wineGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7e273f" />
      <stop offset="100%" stop-color="#5c1529" />
    </linearGradient>
    <filter id="crispFilter" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="1" stdDeviation="0.8" flood-opacity="0.12" flood-color="#34041f" />
    </filter>
  </defs>

  <g transform="translate(0, 0)">
    <!-- CROWN ABOVE 'Z' -->
    <g transform="translate(112, 110) scale(0.65)" fill="url(#goldGrad)">
      <!-- 3-point crown with circular pearls -->
      <circle cx="16" cy="18" r="5" />
      <circle cx="48" cy="8" r="5.5" />
      <circle cx="80" cy="18" r="5" />
      <path d="M 16 23 
               C 22 45, 24 52, 22 55 
               L 74 55 
               C 72 52, 74 45, 80 23 
               C 66 38, 56 36, 48 14 
               C 40 36, 30 38, 16 23 Z" />
      <rect x="21" y="56" width="54" height="4" rx="2" />
    </g>

    <!-- WOMAN PROFILE & HAIR BUN ABOVE 'I' (Centered at x=300) -->
    <g transform="translate(262, 38) scale(1.15)" fill="url(#goldGrad)">
      <!-- Bun at top left -->
      <path d="M 28 32 C 22 25, 14 20, 8 28 C 1 37, 3 48, 12 55 C 20 61, 28 54, 28 46 C 28 40, 28 36, 28 32 Z" />
      <path d="M 12 30 C 18 24, 26 26, 31 34 C 33 38, 32 44, 27 48 C 22 52, 14 48, 12 42 C 10 38, 10 34, 12 30 Z" fill="#fdf8f1" opacity="0.25"/>

      <!-- Top & back of head / hair waves -->
      <path d="M 28 35 
               C 38 18, 58 20, 68 32 
               C 76 42, 78 52, 70 56 
               C 62 60, 52 48, 42 42 
               C 34 38, 28 36, 28 35 Z" />

      <!-- Sweeping hair strands / volume -->
      <path d="M 18 52 
               C 28 46, 44 46, 56 56 
               C 65 64, 66 74, 58 76 
               C 48 78, 38 68, 26 64 
               C 20 62, 18 56, 18 52 Z" />

      <path d="M 22 65 
               C 32 60, 48 62, 54 74 
               C 58 82, 54 90, 46 94 
               C 38 98, 30 88, 24 80 
               C 20 74, 20 70, 22 65 Z" />

      <!-- Facial profile (Forehead, delicate nose, lips, chin, jawline) -->
      <path d="M 68 32 
               C 72 38, 76 46, 76 52 
               C 74 54, 73 55, 71 56 
               C 74 60, 77 64, 82 68
               C 80 70, 75 72, 73 73 
               C 75 75, 77 77, 75 79 
               C 72 81, 68 81, 66 82 
               C 68 85, 68 87, 65 89 
               C 60 92, 54 92, 50 95 
               C 44 100, 40 108, 38 120 
               C 36 128, 38 138, 42 148 
               C 37 136, 32 122, 30 108 
               C 28 96, 32 86, 38 78 
               C 44 70, 52 66, 56 58 
               C 58 54, 58 48, 54 44 
               C 50 40, 42 36, 36 36 
               C 46 30, 58 28, 68 32 Z" />
    </g>

    <!-- 'ZAISA' LUXURY TYPOGRAPHY -->
    <g fill="url(#wineGrad)">
      <!-- Z -->
      <path d="M 85 160 L 175 160 L 175 174 L 118 246 L 180 246 L 180 262 L 80 262 L 80 248 L 138 176 L 85 176 Z" />

      <!-- A -->
      <path d="M 215 160 L 235 160 L 275 262 L 254 262 L 244 235 L 206 235 L 196 262 L 175 262 Z 
               M 225 182 L 211 221 L 239 221 Z" />

      <!-- I (Positioned directly under the hair strand) -->
      <path d="M 292 160 L 312 160 L 312 262 L 292 262 Z" />

      <!-- S -->
      <path d="M 390 185 C 386 172, 374 160, 355 160 C 335 160, 324 172, 324 185 C 324 200, 336 208, 354 214 C 378 222, 392 232, 392 248 C 392 265, 376 276, 354 276 C 330 276, 316 264, 312 248 L 330 244 C 334 256, 342 262, 354 262 C 366 262, 374 256, 374 246 C 374 234, 364 226, 346 220 C 324 212, 308 202, 308 185 C 308 168, 324 148, 355 148 C 376 148, 392 160, 396 178 Z" />

      <!-- A -->
      <path d="M 435 160 L 455 160 L 495 262 L 474 262 L 464 235 L 426 235 L 416 262 L 395 262 Z 
               M 445 182 L 431 221 L 459 221 Z" />
    </g>

    <!-- 'MAKEOVER' SUBTITLE -->
    <text x="300" y="318" 
          font-family="'Manrope', 'Montserrat', 'Helvetica Neue', sans-serif" 
          font-size="28" 
          font-weight="600" 
          letter-spacing="9" 
          fill="#8e3a44" 
          text-anchor="middle">MAKEOVER</text>
  </g>
</svg>
"""

with open('static/logo.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("Created static/logo.svg")
