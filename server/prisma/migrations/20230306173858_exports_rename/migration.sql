/*
  Warnings:

  - You are about to drop the `Exports` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "Exports" DROP CONSTRAINT "Exports_categoryId_fkey";

-- DropForeignKey
ALTER TABLE "Exports" DROP CONSTRAINT "Exports_userId_fkey";

-- DropTable
DROP TABLE "Exports";

-- CreateTable
CREATE TABLE "ExportItem" (
    "id" SERIAL NOT NULL,
    "weight" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "exportDate" DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "categoryId" INTEGER NOT NULL,
    "donatedTo" TEXT NOT NULL,
    "userId" INTEGER NOT NULL,

    CONSTRAINT "ExportItem_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "ExportItem" ADD CONSTRAINT "ExportItem_categoryId_fkey" FOREIGN KEY ("categoryId") REFERENCES "Category"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "ExportItem" ADD CONSTRAINT "ExportItem_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
