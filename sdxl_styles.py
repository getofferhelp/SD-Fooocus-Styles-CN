# https://github.com/twri/sdxl_prompt_styler/blob/main/sdxl_styles.json

styles = [
    {
        "name": "None",
        "prompt": "{prompt}",
        "negative_prompt": ""
    },
    {
        "name": "默认电影风格cinematic-default",
        "prompt": "cinematic still {prompt} . emotional, harmonious, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy",
        "negative_prompt": "anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured"
    },
    {
        "name": "三维模型风格sai-3d-model",
        "prompt": "professional 3d model {prompt} . octane render, highly detailed, volumetric, dramatic lighting",
        "negative_prompt": "ugly, deformed, noisy, low poly, blurry, painting"
    },
    {
        "name": "胶片风格sai-analog film",
        "prompt": "analog film photo {prompt} . faded film, desaturated, 35mm photo, grainy, vignette, vintage, Kodachrome, Lomography, stained, highly detailed, found footage",
        "negative_prompt": "painting, drawing, illustration, glitch, deformed, mutated, cross-eyed, ugly, disfigured"
    },
    {
        "name": "动漫风格sai-anime",
        "prompt": "anime artwork {prompt} . anime style, key visual, vibrant, studio anime,  highly detailed",
        "negative_prompt": "photo, deformed, black and white, realism, disfigured, low contrast"
    },
    {
        "name": "电影风格sai-cinematic",
        "prompt": "cinematic film still {prompt} . shallow depth of field, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy",
        "negative_prompt": "anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured"
    },
    {
        "name": "漫画风格sai-comic book",
        "prompt": "comic {prompt} . graphic illustration, comic art, graphic novel art, vibrant, highly detailed",
        "negative_prompt": "photograph, deformed, glitch, noisy, realistic, stock photo"
    },
    {
        "name": "橡皮泥风格sai-craft clay",
        "prompt": "play-doh style {prompt} . sculpture, clay art, centered composition, Claymation",
        "negative_prompt": "sloppy, messy, grainy, highly detailed, ultra textured, photo"
    },
    {
        "name": "数码艺术风格sai-digital art",
        "prompt": "concept art {prompt} . digital artwork, illustrative, painterly, matte painting, highly detailed",
        "negative_prompt": "photo, photorealistic, realism, ugly"
    },
    {
        "name": "强化风格sai-enhance",
        "prompt": "breathtaking {prompt} . award-winning, professional, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, distorted, grainy"
    },
{
        "name": "奇幻艺术风格sai-fantasy art",
        "prompt": "ethereal fantasy concept art of  {prompt} . magnificent, celestial, ethereal, painterly, epic, majestic, magical, fantasy art, cover art, dreamy",
        "negative_prompt": "photographic, realistic, realism, 35mm film, dslr, cropped, frame, text, deformed, glitch, noise, noisy, off-center, deformed, cross-eyed, closed eyes, bad anatomy, ugly, disfigured, sloppy, duplicate, mutated, black and white"
    },
    {
        "name": "等轴投影风格sai-isometric",
        "prompt": "isometric style {prompt} . vibrant, beautiful, crisp, detailed, ultra detailed, intricate",
        "negative_prompt": "deformed, mutated, ugly, disfigured, blur, blurry, noise, noisy, realistic, photographic"
    },
    {
        "name": "线描艺术风格sai-line art",
        "prompt": "line art drawing {prompt} . professional, sleek, modern, minimalist, graphic, line art, vector graphics",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, blurry, noisy, off-center, deformed, cross-eyed, closed eyes, bad anatomy, ugly, disfigured, mutated, realism, realistic, impressionism, expressionism, oil, acrylic"
    },
    {
        "name": "低多边形风格sai-lowpoly",
        "prompt": "low-poly style {prompt} . low-poly game art, polygon mesh, jagged, blocky, wireframe edges, centered composition",
        "negative_prompt": "noisy, sloppy, messy, grainy, highly detailed, ultra textured, photo"
    },
    {
        "name": "霓虹未来风格sai-neonpunk",
        "prompt": "neonpunk style {prompt} . cyberpunk, vaporwave, neon, vibes, vibrant, stunningly beautiful, crisp, detailed, sleek, ultramodern, magenta highlights, dark purple shadows, high contrast, cinematic, ultra detailed, intricate, professional",
        "negative_prompt": "painting, drawing, illustration, glitch, deformed, mutated, cross-eyed, ugly, disfigured"
    },
    {
        "name": "折纸艺术风格sai-origami",
        "prompt": "origami style {prompt} . paper art, pleated paper, folded, origami art, pleats, cut and fold, centered composition",
        "negative_prompt": "noisy, sloppy, messy, grainy, highly detailed, ultra textured, photo"
    },
    {
        "name": "摄影风格sai-photographic",
        "prompt": "cinematic photo {prompt} . 35mm photograph, film, bokeh, professional, 4k, highly detailed",
        "negative_prompt": "drawing, painting, crayon, sketch, graphite, impressionist, noisy, blurry, soft, deformed, ugly"
    },
    {
        "name": "像素艺术风格sai-pixel art",
        "prompt": "pixel-art {prompt} . low-res, blocky, pixel art style, 8-bit graphics",
        "negative_prompt": "sloppy, messy, blurry, noisy, highly detailed, ultra textured, photo, realistic"
    },
    {
        "name": "纹理风格sai-texture",
        "prompt": "texture {prompt} top down close-up",
        "negative_prompt": "ugly, deformed, noisy, blurry"
    },
    {
        "name": "广告-广告风格ads-advertising",
        "prompt": "Advertising poster style {prompt} . Professional, modern, product-focused, commercial, eye-catching, highly detailed",
        "negative_prompt": "noisy, blurry, amateurish, sloppy, unattractive"
    },
    {
        "name": "广告-汽车风格ads-automotive",
        "prompt": "Automotive advertisement style {prompt} . Sleek, dynamic, professional, commercial, vehicle-focused, high-resolution, highly detailed",
        "negative_prompt": "noisy, blurry, unattractive, sloppy, unprofessional"
    },
    {
        "name": "广告-企业风格ads-corporate",
        "prompt": "Corporate branding style {prompt} . Professional, clean, modern, sleek, minimalist, business-oriented, highly detailed",
        "negative_prompt": "noisy, blurry, grungy, sloppy, cluttered, disorganized"
    },
    {
        "name": "广告-时尚杂志风格ads-fashion editorial",
        "prompt": "Fashion editorial style {prompt} . High fashion, trendy, stylish, editorial, magazine style, professional, highly detailed",
        "negative_prompt": "outdated, blurry, noisy, unattractive, sloppy"
    },
    {
        "name": "广告-美食摄影风格ads-food photography",
        "prompt": "Food photography style {prompt} . Appetizing, professional, culinary, high-resolution, commercial, highly detailed",
        "negative_prompt": "unappetizing, sloppy, unprofessional, noisy, blurry"
    },
    {
        "name": "广告-奢侈品风格ads-luxury",
        "prompt": "Luxury product style {prompt} . Elegant, sophisticated, high-end, luxurious, professional, highly detailed",
        "negative_prompt": "cheap, noisy, blurry, unattractive, amateurish"
    },
    {
        "name": "广告-房地产风格ads-real estate",
        "prompt": "Real estate photography style {prompt} . Professional, inviting, well-lit, high-resolution, property-focused, commercial, highly detailed",
        "negative_prompt": "dark, blurry, unappealing, noisy, unprofessional"
    },
    {
        "name": "广告-零售风格ads-retail",
        "prompt": "Retail packaging style {prompt} . Vibrant, enticing, commercial, product-focused, eye-catching, professional, highly detailed",
        "negative_prompt": "noisy, blurry, amateurish, sloppy, unattractive"
    },
    {
        "name": "艺术风格-抽象artstyle-abstract",
        "prompt": "abstract style {prompt} . non-representational, colors and shapes, expression of feelings, imaginative, highly detailed",
        "negative_prompt": "realistic, photographic, figurative, concrete"
    },
    {
        "name": "艺术风格-抽象表现主义artstyle-abstract expressionism",
        "prompt": "abstract expressionist painting {prompt} . energetic brushwork, bold colors, abstract forms, expressive, emotional",
        "negative_prompt": "realistic, photorealistic, low contrast, plain, simple, monochrome"
    },
    {
        "name": "艺术风格-装饰艺术artstyle-art deco",
        "prompt": "Art Deco style {prompt} . geometric shapes, bold colors, luxurious, elegant, decorative, symmetrical, ornate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, modernist, minimalist"
    }, 
{
        "name": "艺术风格-新艺术运动artstyle-art nouveau",
        "prompt": "Art Nouveau style {prompt} . elegant, decorative, curvilinear forms, nature-inspired, ornate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, modernist, minimalist"
    },
    {
        "name": "艺术风格-构造主义artstyle-constructivist",
        "prompt": "constructivist style {prompt} . geometric shapes, bold colors, dynamic composition, propaganda art style",
        "negative_prompt": "realistic, photorealistic, low contrast, plain, simple, abstract expressionism"
    },
    {
        "name": "艺术风格-立体派artstyle-cubist",
        "prompt": "cubist artwork {prompt} . geometric shapes, abstract, innovative, revolutionary",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "艺术风格-表现主义artstyle-expressionist",
        "prompt": "expressionist {prompt} . raw, emotional, dynamic, distortion for emotional effect, vibrant, use of unusual colors, detailed",
        "negative_prompt": "realism, symmetry, quiet, calm, photo"
    },
    {
        "name": "艺术风格-涂鸦artstyle-graffiti",
        "prompt": "graffiti style {prompt} . street art, vibrant, urban, detailed, tag, mural",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "艺术风格-超写实主义artstyle-hyperrealism",
        "prompt": "hyperrealistic art {prompt} . extremely high-resolution details, photographic, realism pushed to extreme, fine texture, incredibly lifelike",
        "negative_prompt": "simplified, abstract, unrealistic, impressionistic, low resolution"
    },
    {
        "name": "艺术风格-印象派artstyle-impressionist",
        "prompt": "impressionist painting {prompt} . loose brushwork, vibrant color, light and shadow play, captures feeling over form",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "艺术风格-点彩主义artstyle-pointillism",
        "prompt": "pointillism style {prompt} . composed entirely of small, distinct dots of color, vibrant, highly detailed",
        "negative_prompt": "line drawing, smooth shading, large color fields, simplistic"
    },
{
        "name": "艺术风格-波普艺术artstyle-pop art",
        "prompt": "Pop Art style {prompt} . bright colors, bold outlines, popular culture themes, ironic or kitsch",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, minimalist"
    },
    {
        "name": "艺术风格-迷幻artstyle-psychedelic",
        "prompt": "psychedelic style {prompt} . vibrant colors, swirling patterns, abstract forms, surreal, trippy",
        "negative_prompt": "monochrome, black and white, low contrast, realistic, photorealistic, plain, simple"
    },
    {
        "name": "艺术风格-文艺复兴artstyle-renaissance",
        "prompt": "Renaissance style {prompt} . realistic, perspective, light and shadow, religious or mythological themes, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, modernist, minimalist, abstract"
    },
    {
        "name": "艺术风格-蒸汽朋克artstyle-steampunk",
        "prompt": "steampunk style {prompt} . antique, mechanical, brass and copper tones, gears, intricate, detailed",
        "negative_prompt": "deformed, glitch, noisy, low contrast, anime, photorealistic"
    },
    {
        "name": "艺术风格-超现实主义artstyle-surrealist",
        "prompt": "surrealist art {prompt} . dreamlike, mysterious, provocative, symbolic, intricate, detailed",
        "negative_prompt": "anime, photorealistic, realistic, deformed, glitch, noisy, low contrast"
    },
    {
        "name": "艺术风格-字体艺术artstyle-typography",
        "prompt": "typographic art {prompt} . stylized, intricate, detailed, artistic, text-based",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "艺术风格-水彩画artstyle-watercolor",
        "prompt": "watercolor painting {prompt} . vibrant, beautiful, painterly, detailed, textural, artistic",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "未来主义-生物机械futuristic-biomechanical",
        "prompt": "biomechanical style {prompt} . blend of organic and mechanical elements, futuristic, cybernetic, detailed, intricate",
        "negative_prompt": "natural, rustic, primitive, organic, simplistic"
    },
    {
        "name": "未来主义-生物机械-赛博朋克futuristic-biomechanical cyberpunk",
        "prompt": "biomechanical cyberpunk {prompt} . cybernetics, human-machine fusion, dystopian, organic meets artificial, dark, intricate, highly detailed",
        "negative_prompt": "natural, colorful, deformed, sketch, low contrast, watercolor"
    },
{
        "name": "未来主义-智能化futuristic-cybernetic",
        "prompt": "cybernetic style {prompt} . futuristic, technological, cybernetic enhancements, robotics, artificial intelligence themes",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, historical, medieval"
    },
    {
        "name": "未来主义-智能化机器人futuristic-cybernetic robot",
        "prompt": "cybernetic robot {prompt} . android, AI, machine, metal, wires, tech, futuristic, highly detailed",
        "negative_prompt": "organic, natural, human, sketch, watercolor, low contrast"
    },
    {
        "name": "未来主义-赛博朋克城市景观futuristic-cyberpunk cityscape",
        "prompt": "cyberpunk cityscape {prompt} . neon lights, dark alleys, skyscrapers, futuristic, vibrant colors, high contrast, highly detailed",
        "negative_prompt": "natural, rural, deformed, low contrast, black and white, sketch, watercolor"
    },
    {
        "name": "未来主义-未来主义futuristic-futuristic",
        "prompt": "futuristic style {prompt} . sleek, modern, ultramodern, high tech, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, vintage, antique"
    },
    {
        "name": "未来主义-复古赛博朋克futuristic-retro cyberpunk",
        "prompt": "retro cyberpunk {prompt} . 80's inspired, synthwave, neon, vibrant, detailed, retro futurism",
        "negative_prompt": "modern, desaturated, black and white, realism, low contrast"
    },
    {
        "name": "未来主义-复古未来主义futuristic-retro futurism",
        "prompt": "retro-futuristic {prompt} . vintage sci-fi, 50s and 60s style, atomic age, vibrant, highly detailed",
        "negative_prompt": "contemporary, realistic, rustic, primitive"
    },
    {
        "name": "未来主义-科幻futuristic-sci-fi",
        "prompt": "sci-fi style {prompt} . futuristic, technological, alien worlds, space themes, advanced civilizations",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, historical, medieval"
    },
    {
        "name": "未来主义-蒸汽波futuristic-vaporwave",
        "prompt": "vaporwave style {prompt} . retro aesthetic, cyberpunk, vibrant, neon colors, vintage 80s and 90s style, highly detailed",
        "negative_prompt": "monochrome, muted colors, realism, rustic, minimalist, dark"
    },

{
        "name": "游戏-泡泡龙game-bubble bobble",
        "prompt": "Bubble Bobble style {prompt} . 8-bit, cute, pixelated, fantasy, vibrant, reminiscent of Bubble Bobble game",
        "negative_prompt": "realistic, modern, photorealistic, violent, horror"
    },
    {
        "name": "游戏-赛博朋克game-cyberpunk game",
        "prompt": "cyberpunk game style {prompt} . neon, dystopian, futuristic, digital, vibrant, detailed, high contrast, reminiscent of cyberpunk genre video games",
        "negative_prompt": "historical, natural, rustic, low detailed"
    },
    {
        "name": "游戏-格斗游戏game-fighting game",
        "prompt": "fighting game style {prompt} . dynamic, vibrant, action-packed, detailed character design, reminiscent of fighting video games",
        "negative_prompt": "peaceful, calm, minimalist, photorealistic"
    },
    {
        "name": "游戏-GTA风格game-gta",
        "prompt": "GTA-style artwork {prompt} . satirical, exaggerated, pop art style, vibrant colors, iconic characters, action-packed",
        "negative_prompt": "realistic, black and white, low contrast, impressionist, cubist, noisy, blurry, deformed"
    },
    {
        "name": "游戏-马里奥game-mario",
        "prompt": "Super Mario style {prompt} . vibrant, cute, cartoony, fantasy, playful, reminiscent of Super Mario series",
        "negative_prompt": "realistic, modern, horror, dystopian, violent"
    },
    {
        "name": "游戏-Minecraft风格game-minecraft",
        "prompt": "Minecraft style {prompt} . blocky, pixelated, vibrant colors, recognizable characters and objects, game assets",
        "negative_prompt": "smooth, realistic, detailed, photorealistic, noise, blurry, deformed"
    },
    {
        "name": "游戏-宝可梦game-pokemon",
        "prompt": "Pokémon style {prompt} . vibrant, cute, anime, fantasy, reminiscent of Pokémon series",
        "negative_prompt": "realistic, modern, horror, dystopian, violent"
    },
{
        "name": "游戏-复古街机game-retro arcade",
        "prompt": "retro arcade style {prompt} . 8-bit, pixelated, vibrant, classic video game, old school gaming, reminiscent of 80s and 90s arcade games",
        "negative_prompt": "modern, ultra-high resolution, photorealistic, 3D"
    },
    {
        "name": "游戏-复古游戏game-retro game",
        "prompt": "retro game art {prompt} . 16-bit, vibrant colors, pixelated, nostalgic, charming, fun",
        "negative_prompt": "realistic, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "游戏-角色扮演奇幻游戏game-rpg fantasy game",
        "prompt": "role-playing game (RPG) style fantasy {prompt} . detailed, vibrant, immersive, reminiscent of high fantasy RPG games",
        "negative_prompt": "sci-fi, modern, urban, futuristic, low detailed"
    },
    {
        "name": "游戏-策略游戏game-strategy game",
        "prompt": "strategy game style {prompt} . overhead view, detailed map, units, reminiscent of real-time strategy video games",
        "negative_prompt": "first-person view, modern, photorealistic"
    },
    {
        "name": "游戏-街霸game-streetfighter",
        "prompt": "Street Fighter style {prompt} . vibrant, dynamic, arcade, 2D fighting game, highly detailed, reminiscent of Street Fighter series",
        "negative_prompt": "3D, realistic, modern, photorealistic, turn-based strategy"
    },
    {
        "name": "游戏-塞尔达game-zelda",
        "prompt": "Legend of Zelda style {prompt} . vibrant, fantasy, detailed, epic, heroic, reminiscent of The Legend of Zelda series",
        "negative_prompt": "sci-fi, modern, realistic, horror"
    },
    {
        "name": "纸艺-拼贴papercraft-collage",
        "prompt": "collage style {prompt} . mixed media, layered, textural, detailed, artistic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "纸艺-平面剪纸papercraft-flat papercut",
        "prompt": "flat papercut style {prompt} . silhouette, clean cuts, paper, sharp edges, minimalist, color block",
        "negative_prompt": "3D, high detail, noise, grainy, blurry, painting, drawing, photo, disfigured"
    },
    {
        "name": "纸艺-切纸艺术papercraft-kirigami",
        "prompt": "kirigami representation of {prompt} . 3D, paper folding, paper cutting, Japanese, intricate, symmetrical, precision, clean lines",
        "negative_prompt": "painting, drawing, 2D, noisy, blurry, deformed"
    },
    {
        "name": "纸艺-纸浆塑造papercraft-paper mache",
        "prompt": "paper mache representation of {prompt} . 3D, sculptural, textured, handmade, vibrant, fun",
        "negative_prompt": "2D, flat, photo, sketch, digital art, deformed, noisy, blurry"
    },
    {
        "name": "纸艺-纸卷艺术papercraft-paper quilling",
        "prompt": "paper quilling art of {prompt} . intricate, delicate, curling, rolling, shaping, coiling, loops, 3D, dimensional, ornamental",
        "negative_prompt": "photo, painting, drawing, 2D, flat, deformed, noisy, blurry"
    },
    {
        "name": "纸艺-剪纸拼贴papercraft-papercut collage",
        "prompt": "papercut collage of {prompt} . mixed media, textured paper, overlapping, asymmetrical, abstract, vibrant",
        "negative_prompt": "photo, 3D, realistic, drawing, painting, high detail, disfigured"
    },
{
        "name": "纸艺-剪纸影箱papercraft-papercut shadow box",
        "prompt": "3D papercut shadow box of {prompt} . layered, dimensional, depth, silhouette, shadow, papercut, handmade, high contrast",
        "negative_prompt": "painting, drawing, photo, 2D, flat, high detail, blurry, noisy, disfigured"
    },
    {
        "name": "纸艺-叠加剪纸papercraft-stacked papercut",
        "prompt": "stacked papercut art of {prompt} . 3D, layered, dimensional, depth, precision cut, stacked layers, papercut, high contrast",
        "negative_prompt": "2D, flat, noisy, blurry, painting, drawing, photo, deformed"
    },
    {
        "name": "纸艺-厚层剪纸papercraft-thick layered papercut",
        "prompt": "thick layered papercut art of {prompt} . deep 3D, volumetric, dimensional, depth, thick paper, high stack, heavy texture, tangible layers",
        "negative_prompt": "2D, flat, thin paper, low stack, smooth texture, painting, drawing, photo, deformed"
    },
    {
        "name": "摄影-外星人photo-alien",
        "prompt": "alien-themed {prompt} . extraterrestrial, cosmic, otherworldly, mysterious, sci-fi, highly detailed",
        "negative_prompt": "earthly, mundane, common, realistic, simple"
    },
{
        "name": "抽象表现主义Abstract Expressionism",
        "prompt": "Abstract Expressionism Art, {prompt}, High contrast, minimalistic, colorful, stark, dramatic, expressionism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "学院风Academia",
        "prompt": "Academia, {prompt}, preppy Ivy League style, stark, dramatic, chic boarding school, academia",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, grunge, sloppy, unkempt"
    },
    {
        "name": "动作人偶Action Figure",
        "prompt": "Action Figure, {prompt}, plastic collectable action figure, collectable toy action figure",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "可爱的3D角色Adorable 3D Character",
        "prompt": "Adorable 3D Character, {prompt}, 3D render, adorable character, 3D art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, grunge, sloppy, unkempt, photograph, photo, realistic"
    },
    {
        "name": "可爱的可爱Adorable Kawaii",
        "prompt": "Adorable Kawaii, {prompt}, pretty, cute, adorable, kawaii",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, gothic, dark, moody, monochromatic"
    },
    {
        "name": "装饰艺术Art Deco",
        "prompt": "Art Deco, {prompt}, sleek, geometric forms, art deco style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "新艺术Art Nouveau",
        "prompt": "Art Nouveau, beautiful art, {prompt}, sleek, organic forms, long, sinuous, art nouveau style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, industrial, mechanical"
    },
    {
        "name": "星光光环Astral Aura",
        "prompt": "Astral Aura, {prompt}, astral, colorful aura, vibrant energy",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "前卫Avant-garde",
        "prompt": "Avant-garde, {prompt}, unusual, experimental, avant-garde art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },

{
        "name": "巴洛克风格Baroque",
        "prompt": "Baroque, {prompt}, dramatic, exuberant, grandeur, baroque art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "包豪斯风格海报Bauhaus-Style Poster",
        "prompt": "Bauhaus-Style Poster, {prompt}, simple geometric shapes, clean lines, primary colors, Bauhaus-Style Poster",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "蓝图示意图Blueprint Schematic Drawing",
        "prompt": "Blueprint Schematic Drawing, {prompt}, technical drawing, blueprint, schematic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "漫画Caricature",
        "prompt": "Caricature, {prompt}, exaggerated, comical, caricature",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realistic"
    },
    {
        "name": "卡通渲染Cel Shaded Art",
        "prompt": "Cel Shaded Art, {prompt}, 2D, flat color, toon shading, cel shaded style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "角色设计表Character Design Sheet",
        "prompt": "Character Design Sheet, {prompt}, character reference sheet, character turn around",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "古典主义艺术Classicism Art",
        "prompt": "Classicism Art, {prompt}, inspired by Roman and Greek culture, clarity, harmonious, classicism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "色域绘画Color Field Painting",
        "prompt": "Color Field Painting, {prompt}, abstract, simple, geometic, color field painting style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
{
        "name": "彩色铅笔艺术Colored Pencil Art",
        "prompt": "Colored Pencil Art, {prompt}, colored pencil strokes, light color, visible paper texture, colored pencil art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "概念艺术Conceptual Art",
        "prompt": "Conceptual Art, {prompt}, concept art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "构成主义Constructivism",
        "prompt": "Constructivism Art, {prompt}, minimalistic, geometric forms, constructivism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "立体主义Cubism",
        "prompt": "Cubism Art, {prompt}, flat geometric forms, cubism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "达达主义Dadaism",
        "prompt": "Dadaism Art, {prompt}, satirical, nonsensical, dadaism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "黑暗幻想Dark Fantasy",
        "prompt": "Dark Fantasy Art, {prompt}, dark, moody, dark fantasy style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, bright, sunny"
    },
    {
        "name": "黑暗沉闷氛围Dark Moody Atmosphere",
        "prompt": "Dark Moody Atmosphere, {prompt}, dramatic, mysterious, dark moody atmosphere",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, vibrant, colorful, bright"
    },
    {
        "name": "DMT艺术风格DMT Art Style",
        "prompt": "DMT Art Style, {prompt}, bright colors, surreal visuals, swirling patterns, DMT art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
{
        "name": "涂鸦艺术Doodle Art",
        "prompt": "Doodle Art Style, {prompt}, drawing, freeform, swirling patterns, doodle art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "双重曝光Double Exposure",
        "prompt": "Double Exposure Style, {prompt}, double image ghost effect, image combination, double exposure style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "滴漆溅画艺术Dripping Paint Splatter Art",
        "prompt": "Dripping Paint Splatter Art, {prompt}, dramatic, paint drips, splatters, dripping paint",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "表现主义Expressionism",
        "prompt": "Expressionism Art Style, {prompt}, movement, contrast, emotional, exaggerated forms, expressionism art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "褪色拍立得照片Faded Polaroid Photo",
        "prompt": "Faded Polaroid Photo, {prompt}, analog, old faded photo, old polaroid",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, vibrant, colorful"
    },
{
        "name": "野兽派Fauvism",
        "prompt": "Fauvism Art, {prompt}, painterly, bold colors, textured brushwork, fauvism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "扁平2D艺术Flat 2D Art",
        "prompt": "Flat 2D Art, {prompt}, simple flat color, 2-dimensional, Flat 2D Art Style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, 3D, photo, realistic"
    },
    {
        "name": "堡垒之夜风格Fortnite Art Style",
        "prompt": "Fortnite Art Style, {prompt}, 3D cartoon, colorful, Fortnite Art Style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photo, realistic"
    },
    {
        "name": "未来主义Futurism",
        "prompt": "Futurism Art Style, {prompt}, dynamic, dramatic, Futurism Art Style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "故障艺术风格Glitchcore",
        "prompt": "Glitchcore Art Style, {prompt}, dynamic, dramatic, distorted, vibrant colors, glitchcore art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Glo-fi艺术风格Glo-fi",
        "prompt": "Glo-fi Art Style, {prompt}, dynamic, dramatic, vibrant colors, glo-fi art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
{
        "name": "Googie艺术风格Googie Art Style",
        "prompt": "Googie Art Style, {prompt}, dynamic, dramatic, 1950's futurism, bold boomerang angles, Googie art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "涂鸦艺术Graffiti Art",
        "prompt": "Graffiti Art Style, {prompt}, dynamic, dramatic, vibrant colors, graffiti art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "哈莱姆文艺复兴艺术Harlem Renaissance Art",
        "prompt": "Harlem Renaissance Art Style, {prompt}, dynamic, dramatic, 1920s African American culture, Harlem Renaissance art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "高级时尚High Fashion",
        "prompt": "High Fashion, {prompt}, dynamic, dramatic, haute couture, elegant, ornate clothing, High Fashion",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "田园诗Idyllic",
        "prompt": "Idyllic, {prompt}, peaceful, happy, pleasant, happy, harmonious, picturesque, charming",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "印象派Impressionism",
        "prompt": "Impressionism, {prompt}, painterly, small brushstrokes, visible brushstrokes, impressionistic style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "信息图绘制Infographic Drawing",
        "prompt": "Infographic Drawing, {prompt}, diagram, infographic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "滴墨绘画Ink Dripping Drawing",
        "prompt": "Ink Dripping Drawing, {prompt}, ink drawing, dripping ink",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, colorful, vibrant"
    },
{
        "name": "日本水墨画Japanese Ink Drawing",
        "prompt": "Japanese Ink Drawing, {prompt}, ink drawing, inkwash, Japanese Ink Drawing",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, colorful, vibrant"
    },
    {
        "name": "整齐摄影Knolling Photography",
        "prompt": "Knolling Photography, {prompt}, flat lay photography, object arrangment, knolling photography",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "明亮愉快氛围Light Cheery Atmosphere",
        "prompt": "Light Cheery Atmosphere, {prompt}, happy, joyful, cheerful, carefree, gleeful, lighthearted, pleasant atmosphere",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, monochromatic, dark, moody"
    },
    {
        "name": "标志设计Logo Design",
        "prompt": "Logo Design, {prompt}, dynamic graphic art, vector art, minimalist, professional logo design",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "奢华优雅Luxurious Elegance",
        "prompt": "Luxurious Elegance, {prompt}, extravagant, ornate, designer, opulent, picturesque, lavish",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "微距摄影Macro Photography",
        "prompt": "Macro Photography, {prompt}, close-up, macro 100mm, macro photography",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "曼多拉艺术Mandola Art",
        "prompt": "Mandola art style, {prompt}, complex, circular design, mandola",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "马克笔绘画Marker Drawing",
        "prompt": "Marker Drawing, {prompt}, bold marker lines, visibile paper texture, marker drawing",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photograph, realistic"
    },
    {
        "name": "中世纪主义Medievalism",
        "prompt": "Medievalism, {prompt}, inspired by The Middle Ages, medieval art, elaborate patterns and decoration, Medievalism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "极简主义Minimalism",
        "prompt": "Minimalism, {prompt}, abstract, simple geometic shapes, hard edges, sleek contours, Minimalism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "新巴洛克Neo-Baroque",
        "prompt": "Neo-Baroque, {prompt}, ornate and elaborate, dynaimc, Neo-Baroque",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "新拜占庭Neo-Byzantine",
        "prompt": "Neo-Byzantine, {prompt}, grand decorative religious style, Orthodox Christian inspired, Neo-Byzantine",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "新未来主义Neo-Futurism",
        "prompt": "Neo-Futurism, {prompt}, high-tech, curves, spirals, flowing lines, idealistic future, Neo-Futurism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "新印象派Neo-Impressionism",
        "prompt": "Neo-Impressionism, {prompt}, tiny dabs of color, Pointillism, painterly, Neo-Impressionism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photograph, realistic"
    },
    {
        "name": "新洛可可Neo-Rococo",
        "prompt": "Neo-Rococo, {prompt}, curved forms, naturalistic ornamentation, elaborate, decorative, gaudy, Neo-Rococo",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "新古典主义Neoclassicism",
        "prompt": "Neoclassicism, {prompt}, ancient Rome and Greece inspired, idealic, sober colors, Neoclassicism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
{
        "name": "视错觉艺术Op Art",
        "prompt": "Op Art, {prompt}, optical illusion, abstract, geometric pattern, impression of movement, Op Art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "华丽精细Ornate and Intricate",
        "prompt": "Ornate and Intricate, {prompt}, decorative, highly detailed, elaborate, ornate, intricate",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "铅笔素描Pencil Sketch Drawing",
        "prompt": "Pencil Sketch Drawing, {prompt}, black and white drawing, graphite drawing",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "波普艺术2Pop Art 2",
        "prompt": "Pop Art, {prompt}, vivid colors, flat color, 2D, strong lines, Pop Art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photo, realistic"
    },
    {
        "name": "洛可可Rococo",
        "prompt": "Rococo, {prompt}, flamboyant, pastel colors, curved lines, elaborate detail, Rococo",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "剪影艺术Silhouette Art",
        "prompt": "Silhouette Art, {prompt}, high contrast, well defined, Silhouette Art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "简洁矢量艺术Simple Vector Art",
        "prompt": "Simple Vector Art, {prompt}, 2D flat, simple shapes, minimalistic, professional graphic, flat color, high contrast, Simple Vector Art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, 3D, photo, realistic"
    },
    {
        "name": "Sketchup",
        "prompt": "Sketchup, {prompt}, CAD, professional design, Sketchup",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photo, photograph"
    },
{
        "name": "Steampunk 2",
        "prompt": "Steampunk, {prompt}, retrofuturistic science fantasy, steam-powered tech, vintage industry, gears, neo-victorian, steampunk",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "超现实主义Surrealism",
        "prompt": "Surrealism, {prompt}, expressive, dramatic, organic lines and forms, dreamlike and mysterious, Surrealism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realistic"
    },
    {
        "name": "至上主义Suprematism",
        "prompt": "Suprematism, {prompt}, abstract, limited color palette, geometric forms, Suprematism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realistic"
    },
    {
        "name": "Terragen",
        "prompt": "Terragen, {prompt}, beautiful massive landscape, epic scenery, Terragen",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "宁静放松氛围Tranquil Relaxing Atmosphere",
        "prompt": "Tranquil Relaxing Atmosphere, {prompt}, calming style, soothing colors, peaceful, idealic, Tranquil Relaxing Atmosphere",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, oversaturated"
    },
    {
        "name": "贴纸设计Sticker Designs",
        "prompt": "Vector Art Stickers, {prompt}, professional vector design, sticker designs, Sticker Sheet",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "鲜明边缘光Vibrant Rim Light",
        "prompt": "Vibrant Rim Light, {prompt}, bright rim light, high contrast, bold edge light",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "体积光Volumetric Lighting",
        "prompt": "Volumetric Lighting, {prompt}, light depth, dramatic atmospheric lighting, Volumetric Lighting",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "水彩2Watercolor 2",
        "prompt": "Watercolor style painting, {prompt}, visible paper texture, colorwash, watercolor",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photo, realistic"
    },

    
    {
        "name": "其他-建筑misc-architectural",
        "prompt": "architectural style {prompt} . clean lines, geometric shapes, minimalist, modern, architectural drawing, highly detailed",
        "negative_prompt": "curved lines, ornate, baroque, abstract, grunge"
    },
    {
        "name": "其他-迪斯科misc-disco",
        "prompt": "disco-themed {prompt} . vibrant, groovy, retro 70s style, shiny disco balls, neon lights, dance floor, highly detailed",
        "negative_prompt": "minimalist, rustic, monochrome, contemporary, simplistic"
    },
{
        "name": "其他-梦境misc-dreamscape",
        "prompt": "dreamscape {prompt} . surreal, ethereal, dreamy, mysterious, fantasy, highly detailed",
        "negative_prompt": "realistic, concrete, ordinary, mundane"
    },
    {
        "name": "其他-末日世界misc-dystopian",
        "prompt": "dystopian style {prompt} . bleak, post-apocalyptic, somber, dramatic, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, cheerful, optimistic, vibrant, colorful"
    },
    {
        "name": "其他-童话故事misc-fairy tale",
        "prompt": "fairy tale {prompt} . magical, fantastical, enchanting, storybook style, highly detailed",
        "negative_prompt": "realistic, modern, ordinary, mundane"
    },
    {
        "name": "其他-哥特风格misc-gothic",
        "prompt": "gothic style {prompt} . dark, mysterious, haunting, dramatic, ornate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, cheerful, optimistic"
    },
    {
        "name": "其他-垃圾风格misc-grunge",
        "prompt": "grunge style {prompt} . textured, distressed, vintage, edgy, punk rock vibe, dirty, noisy",
        "negative_prompt": "smooth, clean, minimalist, sleek, modern, photorealistic"
    },
    {
        "name": "其他-可爱misc-kawaii",
        "prompt": "kawaii style {prompt} . cute, adorable, brightly colored, cheerful, anime influence, highly detailed",
        "negative_prompt": "dark, scary, realistic, monochrome, abstract"
    },
    {
        "name": "其他-漫画风格misc-manga",
        "prompt": "manga style {prompt} . vibrant, high-energy, detailed, iconic, Japanese comic style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, Western comic style"
    },
    {
        "name": "其他-大都会风格misc-metropolis",
        "prompt": "metropolis-themed {prompt} . urban, cityscape, skyscrapers, modern, futuristic, highly detailed",
        "negative_prompt": "rural, natural, rustic, historical, simple"
    },
    {
        "name": "其他-简约风格misc-minimalist",
        "prompt": "minimalist style {prompt} . simple, clean, uncluttered, modern, elegant",
        "negative_prompt": "ornate, complicated, highly detailed, cluttered, disordered, messy, noisy"
    },
    {
        "name": "其他-单色调misc-monochrome",
        "prompt": "monochrome {prompt} . black and white, contrast, tone, texture, detailed",
        "negative_prompt": "colorful, vibrant, noisy, blurry, deformed"
    },
    {
        "name": "其他-航海misc-nautical",
        "prompt": "nautical-themed {prompt} . sea, ocean, ships, maritime, beach, marine life, highly detailed",
        "negative_prompt": "landlocked, desert, mountains, urban, rustic"
    },
    {
        "name": "其他-太空misc-space",
        "prompt": "space-themed {prompt} . cosmic, celestial, stars, galaxies, nebulas, planets, science fiction, highly detailed",
        "negative_prompt": "earthly, mundane, ground-based, realism"
    },
{
        "name": "其他-玻璃彩绘misc-stained glass",
        "prompt": "stained glass style {prompt} . vibrant, beautiful, translucent, intricate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "其他-科技服装misc-techwear fashion",
        "prompt": "techwear fashion {prompt} . futuristic, cyberpunk, urban, tactical, sleek, dark, highly detailed",
        "negative_prompt": "vintage, rural, colorful, low contrast, realism, sketch, watercolor"
    },
    {
        "name": "其他-部落风格misc-tribal",
        "prompt": "tribal style {prompt} . indigenous, ethnic, traditional patterns, bold, natural colors, highly detailed",
        "negative_prompt": "modern, futuristic, minimalist, pastel"
    },
    {
        "name": "其他-禅绕misc-zentangle",
        "prompt": "zentangle {prompt} . intricate, abstract, monochrome, patterns, meditative, highly detailed",
        "negative_prompt": "colorful, representative, simplistic, large fields of color"
    },
    {
        "name": "奇幻与好玩Whimsical and Playful",
        "prompt": "Whimsical and Playful, {prompt}, imaginative, fantastical, bight colors, stylized, happy, Whimsical and Playful",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, drab, boring, moody"
    },    
    {
        "name": "其他-恐怖(不建议轻易尝试)misc-horror",
        "prompt": "horror-themed {prompt} . eerie, unsettling, dark, spooky, suspenseful, grim, highly detailed",
        "negative_prompt": "cheerful, bright, vibrant, light-hearted, cute"
    },
    {
        "name": "其他-Lovecraft(不建议轻易尝试)风格misc-lovecraftian",
        "prompt": "lovecraftian horror {prompt} . eldritch, cosmic horror, unknown, mysterious, surreal, highly detailed",
        "negative_prompt": "light-hearted, mundane, familiar, simplistic, realistic"
    },
{
        "name": "其他-恐怖(不建议轻易尝试)macabre",
        "prompt": "macabre style {prompt} . dark, gothic, grim, haunting, highly detailed",
        "negative_prompt": "bright, cheerful, light-hearted, cartoonish, cute"
    }


]

styles = {k['name']: (k['prompt'], k['negative_prompt']) for k in styles}
default_style = styles['None']
style_keys = list(styles.keys())

SD_XL_BASE_RATIOS = {
    "0.5": (704, 1408),
    "0.52": (704, 1344),
    "0.57": (768, 1344),
    "0.6": (768, 1280),
    "0.68": (832, 1216),
    "0.72": (832, 1152),
    "0.78": (896, 1152),
    "0.82": (896, 1088),
    "0.88": (960, 1088),
    "0.94": (960, 1024),
    "1.0": (1024, 1024),
    "1.07": (1024, 960),
    "1.13": (1088, 960),
    "1.21": (1088, 896),
    "1.29": (1152, 896),
    "1.38": (1152, 832),
    "1.46": (1216, 832),
    "1.67": (1280, 768),
    "1.75": (1344, 768),
    "1.91": (1344, 704),
    "2.0": (1408, 704),
    "2.09": (1472, 704),
    "2.4": (1536, 640),
    "2.5": (1600, 640),
    "2.89": (1664, 576),
    "3.0": (1728, 576),
}

aspect_ratios = {str(v[0]) + '×' + str(v[1]): v for k, v in SD_XL_BASE_RATIOS.items()}


def apply_style(style, positive, negative):
    p, n = styles.get(style, default_style)
    return p.replace('{prompt}', positive), n + ', ' + negative
