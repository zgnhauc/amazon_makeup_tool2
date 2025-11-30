# do not sort lists alphabetically, numerically, etc. a specific index in each list should correspond to the same product. for example, the price at index 2 in prices list should be the price for the product name at index 2 of names list
oilyProducts = {
  'names': ['name1', 'name2', 'nameN'],
  'prices': [1.00, 2.00, 45.98],
  'reviews': [oilyName1ReviewList, oilyName2ReviewList, oilyNameNReviewList] # each list should contain three reviews of a product
}

normalProducts = {
  'names': ['name1', 'name2', 'nameN'],
  'prices': [1.00, 2.00, 45.98],
  'reviews': [normalName1ReviewList, normalName2ReviewList, normalNameNReviewList] # each list should contain three reviews of a product
}

dryProducts = {
  'names': ['name1', 'name2', 'nameN'],
  'prices': [1.00, 2.00, 45.98],
  'reviews': [dryName1ReviewList, dryName2ReviewList, dryNameNReviewList] # each list should contain three reviews of a product
}
