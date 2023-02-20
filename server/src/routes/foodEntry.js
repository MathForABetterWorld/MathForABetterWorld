// Guide: https://www.prisma.io/docs/concepts/components/prisma-client/crud

router.post("/", validator.isUniqueName, controller.createFoodEntry);

router.get("/", controller.getFoodEntrys);

router.delete("/:id", validator.isFoodEntryId, controller.deleteFoodEntry);