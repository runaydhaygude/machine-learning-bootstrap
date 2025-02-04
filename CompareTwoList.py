import matplotlib.pyplot as plt

def compare_2d(list_a, list_b):

    # Iterate over each row in list_a
    for i in range(len(list_a)):
        # Iterate over each element in the row
        for j in range(len(list_a[i])):
            # Check if the elements are equal
            if list_a[i][j] == list_b[i][j]:
                pass
            else:
                # If not equal, return False
                return False

    # If all elements are equal, return True
    return True

# Opening the two images in black and white mode for comparison.
# original_image = open_image_bw('galaxy_m61.png')
# comparison_image = open_image_bw('m61_no_star.png')
original_image = [[4, 5, 6], [7, 8, 9], [10, 11, 12]]
comparison_image = [[4, 5, 6], [7, 8, 9], [10, 11, 12]]
# Compare the two 2D lists representing the images.
comparison_result = compare_2d(original_image, comparison_image)

# Print the result of comparison.
if comparison_result == True:
    print("The image contains a spiral galaxy.")
else:
    print("The image does not contain a spiral galaxy.")

# # Display the two images compared.
# plt.imsave('./output/original.png', original_image, cmap=plt.cm.gray_r)
# plt.imsave('./output/comparison.png', comparison_image, cmap=plt.cm.gray_r)

