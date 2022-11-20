kuvert_area = (0.229*0.324)*2
kuvert_vikt = int(input("Kuvertets ytvikt: "))
affisch_area = (0.297*0.420)*2
affisch_vikt = int(input("Affisch ytvikt: "))
blad_area = 0.210*0.297
blad_vikt = int(input("Bladets ytvikt: "))

total_vikt = (kuvert_area*kuvert_vikt) + (affisch_area*affisch_vikt) + (blad_area*blad_vikt)

print(total_vikt)