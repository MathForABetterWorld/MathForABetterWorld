/*
  Warnings:

  - You are about to drop the `Pallot` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "Pallot" DROP CONSTRAINT "Pallot_companyId_fkey";

-- DropForeignKey
ALTER TABLE "Pallot" DROP CONSTRAINT "Pallot_entryUserId_fkey";

-- DropForeignKey
ALTER TABLE "Pallot" DROP CONSTRAINT "Pallot_rackId_fkey";

-- DropTable
DROP TABLE "Pallot";

-- CreateTable
CREATE TABLE "Pallet" (
    "id" SERIAL NOT NULL,
    "entryUserId" INTEGER NOT NULL,
    "inputDate" DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "expirationDate" DATE,
    "weight" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "companyId" INTEGER NOT NULL,
    "rackId" INTEGER,
    "inWarehouse" BOOLEAN NOT NULL DEFAULT false,
    "description" TEXT,
    "categoryIds" INTEGER[],
    "barcodes" INTEGER[],

    CONSTRAINT "Pallet_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "Pallet" ADD CONSTRAINT "Pallet_entryUserId_fkey" FOREIGN KEY ("entryUserId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Pallet" ADD CONSTRAINT "Pallet_companyId_fkey" FOREIGN KEY ("companyId") REFERENCES "Distributor"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Pallet" ADD CONSTRAINT "Pallet_rackId_fkey" FOREIGN KEY ("rackId") REFERENCES "Rack"("id") ON DELETE SET NULL ON UPDATE CASCADE;
