/*
  Warnings:

  - You are about to drop the `FoodEntry` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "FoodEntry" DROP CONSTRAINT "FoodEntry_categoryId_fkey";

-- DropForeignKey
ALTER TABLE "FoodEntry" DROP CONSTRAINT "FoodEntry_companyId_fkey";

-- DropForeignKey
ALTER TABLE "FoodEntry" DROP CONSTRAINT "FoodEntry_entryUserId_fkey";

-- DropForeignKey
ALTER TABLE "FoodEntry" DROP CONSTRAINT "FoodEntry_rackId_fkey";

-- DropTable
DROP TABLE "FoodEntry";

-- CreateTable
CREATE TABLE "Pallot" (
    "id" SERIAL NOT NULL,
    "entryUserId" INTEGER NOT NULL,
    "inputDate" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "expirationDate" DATE,
    "weight" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "companyId" INTEGER NOT NULL,
    "rackId" INTEGER,
    "inWarehouse" BOOLEAN NOT NULL DEFAULT false,
    "description" TEXT,

    CONSTRAINT "Pallot_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "_CategoryToPallot" (
    "A" INTEGER NOT NULL,
    "B" INTEGER NOT NULL
);

-- CreateIndex
CREATE UNIQUE INDEX "_CategoryToPallot_AB_unique" ON "_CategoryToPallot"("A", "B");

-- CreateIndex
CREATE INDEX "_CategoryToPallot_B_index" ON "_CategoryToPallot"("B");

-- AddForeignKey
ALTER TABLE "Pallot" ADD CONSTRAINT "Pallot_entryUserId_fkey" FOREIGN KEY ("entryUserId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Pallot" ADD CONSTRAINT "Pallot_companyId_fkey" FOREIGN KEY ("companyId") REFERENCES "Distributor"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Pallot" ADD CONSTRAINT "Pallot_rackId_fkey" FOREIGN KEY ("rackId") REFERENCES "Rack"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "_CategoryToPallot" ADD CONSTRAINT "_CategoryToPallot_A_fkey" FOREIGN KEY ("A") REFERENCES "Category"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "_CategoryToPallot" ADD CONSTRAINT "_CategoryToPallot_B_fkey" FOREIGN KEY ("B") REFERENCES "Pallot"("id") ON DELETE CASCADE ON UPDATE CASCADE;
