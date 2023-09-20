import cv2

def resize_image(image, width=800, height=600):
    return cv2.resize(image, (width, height))

def compare_images(target_image, reference_images):
    target_image = resize_image(target_image)
    unmatched_results = []
    best_match = None
    best_similarity = float('inf')

    reference_names = ["Orion", "Cassiopeia", "Big Dipper"]

    for i, ref_image in enumerate(reference_images):
        ref_image = resize_image(ref_image)
        difference = cv2.absdiff(target_image, ref_image)
        gray_difference = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
        similarity = cv2.mean(gray_difference)[0]

        if similarity < best_similarity:
            if best_match is not None:
                unmatched_results.append((best_match[1], best_similarity))
            best_similarity = similarity
            best_match = (ref_image, reference_names[i])
        else:
            unmatched_results.append((reference_names[i], similarity))

    return unmatched_results, best_match

# Load the target image and reference images
target_image = cv2.imread("1_1.jpg")
reference_images = [cv2.imread("1.jpg"), cv2.imread("2.jpg"), cv2.imread("3.jpg")]

unmatched_results, best_match = compare_images(target_image, reference_images)

for ref_name, similarity in unmatched_results:
    print(f"Unmatched image: {ref_name} (Similarity: {similarity:.2f})")

if best_match is not None:
    matched_name = best_match[1]
    print(f"\nMatched image: {matched_name}")

cv2.imshow(f"Matched Image - {matched_name}", best_match[0])
cv2.waitKey(0)
cv2.destroyAllWindows()