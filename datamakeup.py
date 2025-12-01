# do not sort lists alphabetically, numerically, etc. a specific index in each list should correspond to the same product. for example, the price at index 2 in prices list should be the price for the product name at index 2 of names list
oilyProducts = {
  'names': ['The Ordinary The Acne Set, 3-Step Skin Regimen with Glucoside Foaming Cleanser, Salicylic Acid 2% Solution, and Natural Moisturizing Factors + Beta Glucan',
            'The Ordinary Niacinamide 10% + Zinc 1%, Smoothing Serum for Blemish-Prone Skin',
            'CeraVe Foaming Facial Cleanser, Daily Face Wash for Oily Skin, Hyaluronic Acid + Ceramides + Niacinamide, Fragrance Free & Paraben Free, Non-Drying Oil Control Face Wash, 19 Fluid Ounce'
            'CeraVe Oil Control Moisturizing Gel-Cream, Face Moisturizer for Oily Skin, Niacinamide, Hyaluronic Acid & Oil Absorbing Technology To Rebalance Oily Skin, Non-Comedogenic, Fragrance Free & Oil-Free',
            'La Roche-Posay Effaclar Purifying Foaming Gel Cleanser for Oily Skin, 13.5 Fluid Ounce',
            'Neutrogena Hydro Boost Water Gel, Face Moisturizer for Dry Skin with Hyaluronic Acid, Oil-Free, Non-Comedogenic, Fragrance Free, 1.7 oz',
            'La Roche-Posay Serozinc Face Toner for Oily Skin with Zinc, Mattifying Face Spray and Acne Prone Skin Toner to Reduce Shine for Oil Control, Alcohol Free Face Mist, 5 Fl Oz (Pack of 1)',
            'CeraVe Resurfacing Retinol Serum For Post Acne Marks, Formulated With Licorice Root Extract & Niacinamide, Brightening Serum & Pore Minimizer For Face, Post Acne Skin Barrier Repair, Non-Comedogenic',
            'Teenitor 400 Counts Oil Blotting Papers for Face, Bamboo Charcoal Oil Absorbing Sheets for Oily Skin, Oil Blotting Sheets for Face, Oil Absorbent Pads Blotter Paper, Oil Face Wipes Large 10cmx7cm',
            'Medicube Zero Pore Pads 2.0, Dual-Textured Facial Toner Pads for Exfoliation and Pore Care with 4.5% AHA Lactic Acid & 0.45% BHA Salicylic Acid, Ideal for All Skin Types, Korean Skin Care (70 units)',
            'PanOxyl Acne Foaming Wash Benzoyl Peroxide 10% Maximum Strength Antimicrobial, 5.5 Oz',
            'Biore Deep Pore Charcoal Face Wash, Daily Facial Cleanser for Dirt & Makeup Removal, for Oily Skin, 6.77 Oz',
            'Anua Heartleaf Pore Control Cleansing Oil, Oil Cleanser for Face, Makeup Blackhead Remover, Korean Skin Care 6.76 fl oz(200ml) (original)',
            'Inkey List Salicylic Acid Cleanser, Acne Face Wash for Oily and Blemish-Prone Skin, 6.76 fl oz',
            'La Roche-Posay Effaclar Duo Dual Action Acne Treatment with Benzoyl',
            'The Inkey List Niacinamide, Oil Control Serum for Blemish-Prone Skin, 1 fl oz',
            'Paula\'s Choice CLEAR Pore Normalizing Cleanser for Acne-Prone Skin',
            'Neutrogena Oil-Free Acne Wash, Facial Cleanser with Salicylic Acid for Acne-Prone Skin, 6.7 fl. oz',
            'COSRX Low pH Good Morning Gel Cleanser for Face, Gentle Daily Face Wash for Oily and Combination Skin, 150ml/5.07 fl. oz',
            'Murad Clarifying Cleanser for Acne-Prone Skin, 6.75 fl. oz'
            'La Roche-Posay Pure 12% Vitamin C Serum For Face With Hyaluronic Acid & Salicylic Acid, Hydrating Face Serum, Boost Radiance & Reduce Wrinkles, 2 Formulas for Normal or Oily Skin Control',
            'Minimalist 2% Salicylic Acid Serum For Acne, Blackhead & Open Pores | Reduces Excess Oil & Bumpy Texture | BHA Liquid Exfoliant for Acne Prone & Oily Skin | For Women & Men | 1 Fl Oz/30ml' ],
 
  'prices': [15.80, 6.00, 7.04, 9.98, 12.03, 16.97, 10.99, 19.99, 5.99, 22.00, 9.97, 8.97, 14.99, 7.99, 18.99, 7.99, 10.00, 7.97, 11.00, 12.00, 29.99, 14.99],
  'reviews': ['Customers find the skincare set effective at minimizing acne breakouts and improving skin clarity, while being gentle and affordable. The product receives positive feedback for its hydrating properties, leaving skin soft and smooth, and customers appreciate its effectiveness. Regarding skin protection, while some find it good for sensitive skin, others report it stings and burns. The size of the product receives mixed reviews, with several customers noting it's smaller than expected.', oilyName2ReviewList, oilyNameNReviewList] # each list should contain three reviews of a product',
              'Customers find this skincare set effective, with the cleanser gently removing makeup and impurities, and the moisturizer keeping skin hydrated throughout the day. The products receive positive feedback for their quality and value for money, and customers report their skin feels smoother and more refreshed after use. While the hyaluronic acid serum is full size, customers note that the cleanser and moisturizer tubes are only half full, and opinions about skin protection are mixed, with some finding it great for sensitive skin while others experienced rashes.',
              'Customers find the salicylic acid serum effective at clearing skin and keeping it moisturized without being overly oily. The product receives positive feedback for its light weight and smooth texture, and customers consider it good value for money. Regarding skin irritation and stickiness, opinions are mixed - while some find it non-sticky, others report it being very sticky.',
              'Customers find the foaming cleanser effective at removing dirt and oil without over-drying the skin. The product receives positive feedback for its gentle formula and ability to leave skin feeling clean and refreshed. Customers appreciate its value for money, and many report improvements in their skin's texture and appearance after regular use. Regarding skin irritation, most customers find it non-irritating, although a few report mild dryness after use. The size of the product is generally well-received, with customers noting it lasts a long time.',
              'Customers find the oil blotting papers effective, with one noting they work as well as more expensive versions. The product receives positive feedback for its value and ability to keep faces less oily, and one customer mentions it's easy to travel with. The absorbency and quality receive mixed reviews, with some finding them highly absorbent while others consider them horrible, and many noting the sheets are very thin. The ease of removal is a concern, with multiple customers mentioning it's difficult to get just one sheet out.',
              'Customers find the pore pads effective at exfoliating and improving skin texture, with many noting a reduction in blackheads and smoother skin. The product receives positive feedback for its gentle formula and ease of use, and customers appreciate its value for money. Regarding skin irritation, most customers find it non-irritating, although a few report mild redness after use. The size of the product is generally well-received, with customers noting it lasts a long time.',
              'Customers find the acne foaming wash effective at treating breakouts and keeping skin clear, with many noting a reduction in acne and improved skin texture. The product receives positive feedback for its strong formula and ability to deeply cleanse the skin. Customers appreciate its value for money, and many report that it helps prevent future breakouts. Regarding skin irritation, opinions are mixed - while some find it non-irritating, others report dryness and redness after use. The size of the product is generally well-received, with customers noting it lasts a long time.',
              'Customers find this facial cleanser effective for oily and dry skin, noting it clears up skin issues and doesn't overdry or irritate it. The product receives positive feedback for its gentle formula for sensitive skin, leaving skin soft and smooth, and customers appreciate its scentless formula and good value for money. Opinions about the foaming action are mixed, with some saying it foams a lot while others report it doesn't produce any foam at all.',
              'Customers find this moisturizer effective for oily skin, noting it doesn't leave a greasy feeling and provides good hydration. The product has a lightweight gel-cream texture that's smooth under makeup and keeps skin shine-free for hours. While some customers report it doesn't irritate sensitive skin, others mention it can cause burning sensations. The matte finish receives mixed feedback, with some appreciating its subtle effect while others say it doesn't provide a matte look at all.',
              'Customers find the mud mask effective at deep cleaning pores and clearing acne, leaving skin soft and smooth with a glowing complexion. Moreover, the mask dries quickly with a powdery soft finish, and customers appreciate its lovely smell. However, opinions about skin compatibility are mixed - while some find it gentle on sensitive skin, others report irritation.',
              'Customers find the vitamin C serum effective at brightening skin and reducing wrinkles, with many noting improved radiance and texture. The product receives positive feedback for its hydrating properties and ability to even out skin tone. Customers appreciate its value for money, and many report seeing noticeable results after regular use. Regarding skin irritation, most customers find it non-irritating, although a few report mild redness after use. The size of the product is generally well-received, with customers noting it lasts a long time.', 
              'Customers find the mud mask effective at deep cleaning pores and clearing acne, leaving skin soft and smooth with a glowing complexion. Moreover, the mask dries quickly with a powdery soft finish, and customers appreciate its lovely smell. However, opinions about skin compatibility are mixed - while some find it gentle on sensitive skin, others report irritation.',
              'Customers find the mud mask effective at deep cleaning pores and clearing acne, leaving skin soft and smooth with a glowing complexion. Moreover, the mask dries quickly with a powdery soft finish, and customers appreciate its lovely smell. However, opinions about skin compatibility are mixed - while some find it gentle on sensitive skin, others report irritation.', ]
}


normalProducts = {
    'names': [
        'CeraVe Hydrating Facial Cleanser, Daily Moisturizing Cleanser for Normal Skin, 16 fl oz',
        'La Roche-Posay Toleriane Dermal Cleanser, Gentle Face Wash for Normal Skin',
        'Neutrogena Ultra Gentle Daily Cleanser, Foaming Formula for Normal Skin, 12 fl oz',
        'Aveeno Positively Radiant Daily Moisturizer with SPF 30, 4 fl oz',
        'Vanicream Daily Facial Moisturizer for Normal or Sensitive Skin, 3 fl oz',
        'The Ordinary Hyaluronic Acid 2% + B5 Lightweight Hydration Serum',
        'Cetaphil Daily Facial Moisturizer with SPF 15, Normal Skin Formula',
        'Eucerin Advanced Repair Cream, Everyday Moisturizer for Normal Skin, 16 oz',
        'COSRX Advanced Snail 96 Mucin Power Essence, Hydrating Serum for Normal Skin',
        'First Aid Beauty Ultra Repair Cream, Intense Hydration for Normal Skin'
    ],

    'prices': [
        14.97, 19.99, 9.89, 13.59, 11.49,
        8.90, 12.89, 16.50, 18.99, 28.00
    ],

    'reviews': [
        'Customers find this cleanser effective for daily use, noting it removes dirt without stripping moisture. Its gentle formula leaves the skin soft and refreshed, and people appreciate the smooth texture. Some users say it feels slightly too light for deep cleansing, but most consider it reliable for normal skin.',
        'Customers appreciate this gentle wash for maintaining skin balance, reporting no irritation or tightness. The creamy consistency feels soothing, and users note calmer skin after consistent use. Some find the packaging inconvenient, but the product’s performance stays highly rated.',
        'Customers find this cleanser effective at removing impurities without overdrying. The light foaming action feels refreshing, and many report smoother, more even-looking skin. Opinions on scent vary, but overall performance is praised.',
        'Customers enjoy this moisturizer for providing lightweight hydration and daily SPF protection. The brightening effect is well-received, particularly for reducing mild dullness. Some users mention it can pill when layered with serums, but most like its smooth feel under makeup.',
        'Customers find this moisturizer simple and effective, noting it hydrates without greasiness. The non-irritating formula works well for daily use, especially for normal-to-sensitive skin. Some wish it were slightly thicker, but many appreciate the minimal, clean ingredients.',
        'Customers say this hydration serum absorbs quickly and leaves skin refreshed. Many appreciate the plumping effect and smooth finish. Some note it can feel sticky if too much is applied, but overall it layers well with moisturizers.',
        'Customers find this moisturizer lightweight and comfortable for daytime wear. It absorbs quickly, provides basic SPF protection, and feels gentle on normal skin. A few wish the SPF were higher, but most are satisfied with its performance.',
        'Customers find this repair cream deeply hydrating without feeling heavy. It improves rough texture and offers long-lasting moisture. Some mention the scent is slightly medicinal, but effectiveness outweighs this concern.',
        'Customers find this snail essence hydrating and smoothing, with noticeable improvements in skin elasticity. The lightweight texture absorbs well and provides a healthy glow. A few find it slippery, but most love the results.',
        'Customers appreciate this moisturizer for its intense hydration and soothing feel. It absorbs quickly without residue and works well for nighttime moisture. Some find it too rich for mornings, but it remains a favorite for comfort and hydration.'
    ]
}

dryProducts = {
    'names': [
        'CeraVe Moisturizing Cream with Ceramides and Hyaluronic Acid, 19 oz',
        'La Roche-Posay Lipikar Balm AP+ Intense Repair Moisturizer, 13.5 oz',
        'Neutrogena Hydro Boost Gel-Cream for Extra Dry Skin, Hyaluronic Acid, 1.7 oz',
        'Eucerin Advanced Repair Lotion for Very Dry Skin, 16.9 oz',
        'Aveeno Calm + Restore Oat Gel Moisturizer for Dry, Sensitive Skin',
        'The Ordinary 100% Plant-Derived Squalane Lightweight Oil',
        'Cetaphil Rich Hydrating Cream with Hyaluronic Acid for Dry Skin, 1.7 oz',
        'First Aid Beauty Ultra Repair Oatmeal Mask, Soothing Treatment for Dry Skin',
        'Bioderma Atoderm Intensive Balm for Dry and Irritated Skin',
        'Kiehl’s Ultra Facial Cream, 24-Hour Daily Light Moisturizer'
    ],

    'prices': [
        17.89, 18.99, 14.29, 10.99, 11.79,
        7.90, 12.49, 20.00, 18.49, 32.00
    ],

    'reviews': [
        'Customers find this cream extremely hydrating and long-lasting, often restoring moisture overnight. The rich texture absorbs well without greasiness. Some dislike the tub packaging, but most prioritize its strong performance.',
        'Customers appreciate this balm for calming severely dry skin, especially during winter. It reduces flakiness and irritation quickly. Though thick, the formula spreads easily and leaves the skin comfortable for hours.',
        'Customers find this gel-cream lightweight yet deeply hydrating, relieving tightness instantly. The bouncy texture is well-loved, though some report a slightly chemical scent. Overall it performs exceptionally well for dry skin.',
        'Customers appreciate this lotion for providing fast relief to rough, flaky areas. It absorbs quickly and leaves skin soft throughout the day. Some say the texture is runny, but most value the strong moisturization.',
        'Customers find this oat moisturizer soothing and calming, especially during irritation flare-ups. The gel texture absorbs comfortably and feels cooling. Some wish it were richer for very dry skin, but many use it daily.',
        'Customers love this squalane oil for deep hydration and a healthy glow. It softens dry patches quickly and layers well with moisturizers. A few find it slippery for daytime use, but it excels as a nighttime booster.',
        'Customers find this rich cream hydrating and gentle, especially for chronically dry areas. The fragrance-free formula is well-received. Some wish the texture were lighter, but most praise its strong moisture retention.',
        'Customers appreciate this oat mask for soothing redness and restoring hydration. It leaves the skin soft and comforted after rinsing. A few find the consistency thick, but it works very well for dry, irritated skin.',
        'Customers find this balm extremely effective for repairing damaged skin barriers. Many report major improvements within a week. The thick texture absorbs surprisingly well and offers long-lasting comfort.',
        'Customers appreciate this cream for delivering reliable all-day hydration without heaviness. It leaves the skin soft, plump, and smooth. Some find it pricey, but most consider it worth the results.'
    ]
}
