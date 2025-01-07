from FrechetInceptionDistance import FID

genrated_image = 'data/gen3.png'
real_image = 'data/img3.png'

fid_score = FID(genrated_image, real_image)
print(f"FID Score: {fid_score}")