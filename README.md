# Dynamic Social Media Captioner 🔤

An automated kinetic typography script built to maximize viewer retention. By pulling precise word-level alignment arrays from AI models, this script dynamically overlays text tracking onto video frames and alters text colors programmatically when a vital emphasis word is spoken.

### Key Capabilities
- Microsecond-accurate word-level text tracking.
- Custom style matrices for background bounding boxes and modern fonts.
- Automatic emphasis dictionary mapping.

## 🔤 Kinetic Typography Example

### 📥 Word-Level Token Arrays
- `{"word": "This", "start": 0.2, "end": 0.4}`
- `{"word": "AI", "start": 0.4, "end": 0.7}`
- `{"word": "is", "start": 0.7, "end": 0.9}`
- `{"word": "INSANE!", "start": 0.9, "end": 1.4}`

### 🎨 Rendering Engine Rules
- Standard style: White text, Impact font, size 72, black drop-shadow.
- Emphasis dictionary trigger: Match found for `"INSANE!"`. Style modified to bold yellow, size 90, with an automated 1.2x scale-pop animation frame.

### 📤 Output Result
- Words snap onto the screen exactly as they are spoken. The final word **"INSANE!"** flashes brightly in yellow to grip viewer retention.
