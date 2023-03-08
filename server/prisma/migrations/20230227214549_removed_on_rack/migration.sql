/*
  Warnings:

  - You are about to drop the column `onRack` on the `FoodEntry` table. All the data in the column will be lost.
  - Made the column `name` on table `User` required. This step will fail if there are existing NULL values in that column.

*/
-- AlterTable
ALTER TABLE "FoodEntry" DROP COLUMN "onRack";

-- AlterTable
ALTER TABLE "User" ALTER COLUMN "name" SET NOT NULL;
