/*
  Warnings:

  - You are about to drop the column `donatedTo` on the `ExportItem` table. All the data in the column will be lost.
  - Made the column `locationId` on table `ExportItem` required. This step will fail if there are existing NULL values in that column.

*/
-- DropForeignKey
ALTER TABLE "ExportItem" DROP CONSTRAINT "ExportItem_locationId_fkey";

-- AlterTable
ALTER TABLE "ExportItem" DROP COLUMN "donatedTo",
ALTER COLUMN "locationId" SET NOT NULL;

-- AddForeignKey
ALTER TABLE "ExportItem" ADD CONSTRAINT "ExportItem_locationId_fkey" FOREIGN KEY ("locationId") REFERENCES "DonationLocation"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
