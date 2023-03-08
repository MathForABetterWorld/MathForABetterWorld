-- AlterTable
ALTER TABLE "Pallot" ALTER COLUMN "inputDate" SET DATA TYPE DATE;

-- CreateTable
CREATE TABLE "Exports" (
    "id" SERIAL NOT NULL,
    "weight" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "exportDate" DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "categoryId" INTEGER NOT NULL,
    "donatedTo" TEXT NOT NULL,
    "userId" INTEGER NOT NULL,

    CONSTRAINT "Exports_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "Exports" ADD CONSTRAINT "Exports_categoryId_fkey" FOREIGN KEY ("categoryId") REFERENCES "Category"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Exports" ADD CONSTRAINT "Exports_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
