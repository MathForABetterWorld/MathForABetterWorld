-- CreateTable
CREATE TABLE "FoodEntry" (
    "id" SERIAL NOT NULL,
    "entryUserId" INTEGER NOT NULL,
    "inputDate" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "expirationDate" DATE,
    "weight" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "companyId" INTEGER NOT NULL,
    "onRack" BOOLEAN NOT NULL DEFAULT false,
    "inWarehouse" BOOLEAN NOT NULL DEFAULT false,
    "description" TEXT,

    CONSTRAINT "FoodEntry_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "FoodEntry" ADD CONSTRAINT "FoodEntry_entryUserId_fkey" FOREIGN KEY ("entryUserId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "FoodEntry" ADD CONSTRAINT "FoodEntry_companyId_fkey" FOREIGN KEY ("companyId") REFERENCES "Distributor"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
