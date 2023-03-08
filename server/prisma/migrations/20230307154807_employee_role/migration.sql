-- CreateEnum
CREATE TYPE "Role" AS ENUM ('Admin', 'Employee');

-- AlterTable
ALTER TABLE "Employee" ADD COLUMN     "role" "Role" NOT NULL DEFAULT 'Employee';
