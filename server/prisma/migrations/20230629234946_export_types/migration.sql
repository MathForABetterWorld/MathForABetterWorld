-- CreateEnum
CREATE TYPE "ExportType" AS ENUM ('Recycle', 'Compost', 'Regular', 'Damaged');

-- AlterTable
ALTER TABLE "ExportItem" ADD COLUMN     "exportType" "ExportType" NOT NULL DEFAULT 'Regular';

-- AlterTable
ALTER TABLE "User" ADD COLUMN     "isActive" BOOLEAN NOT NULL DEFAULT true;

-- CreateTable
CREATE TABLE "Location" (
    "id" SERIAL NOT NULL,
    "name" TEXT NOT NULL,

    CONSTRAINT "Location_pkey" PRIMARY KEY ("id")
);
