/*
  Warnings:

  - You are about to drop the column `foodTaken` on the `Shift` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE "Shift" DROP COLUMN IF EXISTS "foodTaken",
ADD COLUMN IF NOT EXISTS    "damagedFoodTaken" DOUBLE PRECISION NOT NULL DEFAULT 0,
ADD COLUMN IF NOT EXISTS    "regularFoodTaken" DOUBLE PRECISION NOT NULL DEFAULT 0;
