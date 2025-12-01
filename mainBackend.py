# imports dataset file
from dataset import oilyProducts, normalProducts, dryProducts


# asks user their specifications for 
userSkinType = input("What is your skin type? ")
userSkinType = userSkinType.lower() # makes sure capitalization does not interfere with the if checks later on
userBudget = float(input("What is your budget? "))

# makes empty lists to store suitable product details
suitableProductNames = []
suitableProductPrices = []
suitableProductReviews = []


# will go through all data for user's skin type and filter based on price

if userSkinType == "oily":
    # extracts data from dictionaries in dataset fle and organizes it into lists
    productList = oilyProducts["names"]
    priceList = oilyProducts["prices"]
    reviewList = oilyProducts["reviews"]

    for price in range(len(priceList)): # iterates through all the prices for oily skin products
        if priceList[price] <= userBudget: # if the price of a oily skin product is less than or equal to the user's budget, all it's product details are added to three different lists (prices, product name, product reviews)
            suitableProductPrices.append(priceList[price])
            suitableProductNames.append(productList[price])
            suitableProductReviews.append(reviewList[price])

elif userSkinType == "normal":
    # extracts data from dictionaries in dataset fle and organizes it into lists
    productList = normalProducts["names"]
    priceList = normalProducts["prices"]
    reviewList = normalProducts["reviews"]

    for price in range(len(priceList)): # iterates through all the prices for normal skin products
        if priceList[price] <= userBudget: # if the price of a normal skin product is less than or equal to the user's budget, all it's product details are added to three different lists (prices, product name, product reviews)
            suitableProductPrices.append(priceList[price])
            suitableProductNames.append(productList[price])
            suitableProductReviews.append(reviewList[price])

elif userSkinType == "dry":
    # extracts data from dictionaries in dataset fle and organizes it into lists
    productList = dryProducts["names"]
    priceList = dryProducts["prices"]
    reviewList = dryProducts["reviews"]

    for price in range(len(priceList)): # iterates through all the prices for dry skin products
        if priceList[price] <= userBudget: # if the price of a dry skin product is less than or equal to the user's budget, all it's product details are added to three different lists (prices, product name, product reviews)
            suitableProductPrices.append(priceList[price])
            suitableProductNames.append(productList[price])
            suitableProductReviews.append(reviewList[price])

else: # in case the user enters an invalid skin type
    print("Invalid skin type. Please try again with oily, normal, or dry.")


# all products have been filtered and suitable product specifications have been stored in their respective lists. now will be put to output
if len(suitableProductNames) == 0:
    print("Sorry, no suitable products for your request")
else:
    for i in range(len(suitableProductNames)):
        print("--------------------------------------------------")
        print(f"Product {i+1}")
        print(f"Name: {suitableProductNames[i]}")
        print(f"Price: {suitableProductPrices[i]}")
        print(f"Review: {suitableProductReviews[i]}")
