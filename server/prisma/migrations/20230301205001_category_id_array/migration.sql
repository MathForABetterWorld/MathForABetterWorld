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

CREATE ROLE readaccess;

-- Grant access to existing tables
GRANT USAGE ON SCHEMA public TO readaccess;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readaccess;

-- Grant access to future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO readaccess;

CREATE USER read_credentials WITH PASSWORD 'read_credentials';
GRANT readaccess TO read_credentials;

