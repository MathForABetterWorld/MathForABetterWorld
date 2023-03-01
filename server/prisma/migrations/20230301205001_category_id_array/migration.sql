/*
  Warnings:

  - You are about to drop the `_CategoryToPallot` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "_CategoryToPallot" DROP CONSTRAINT "_CategoryToPallot_A_fkey";

-- DropForeignKey
ALTER TABLE "_CategoryToPallot" DROP CONSTRAINT "_CategoryToPallot_B_fkey";

-- AlterTable
ALTER TABLE "Pallot" ADD COLUMN     "categoryIds" INTEGER[];

-- DropTable
DROP TABLE "_CategoryToPallot";
