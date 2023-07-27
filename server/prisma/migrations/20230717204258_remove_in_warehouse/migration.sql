/*
  Warnings:

  - You are about to drop the column `inWarehouse` on the `Pallet` table. All the data in the column will be lost.
  - You are about to drop the column `foodTaken` on the `Shift` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE "Pallet" DROP COLUMN "inWarehouse";

-- AlterTable
ALTER TABLE "Shift" DROP COLUMN "foodTaken",
ADD COLUMN     "damagedFoodTaken" DOUBLE PRECISION NOT NULL DEFAULT 0,
ADD COLUMN     "regularFoodTaken" DOUBLE PRECISION NOT NULL DEFAULT 0;
