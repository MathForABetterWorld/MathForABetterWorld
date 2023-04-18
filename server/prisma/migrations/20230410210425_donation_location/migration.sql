/*
  Warnings:

  - You are about to drop the `Location` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "ExportItem" DROP CONSTRAINT "ExportItem_locationId_fkey";

-- DropTable
DROP TABLE "Location";

-- CreateTable
CREATE TABLE "DonationLocation" (
    "id" SERIAL NOT NULL,
    "name" TEXT NOT NULL,
    "longitude" TEXT NOT NULL,
    "latitude" TEXT NOT NULL,

    CONSTRAINT "DonationLocation_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "ExportItem" ADD CONSTRAINT "ExportItem_locationId_fkey" FOREIGN KEY ("locationId") REFERENCES "DonationLocation"("id") ON DELETE SET NULL ON UPDATE CASCADE;
