from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "order" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "status" VARCHAR(20) NOT NULL,
    "total_amount" DECIMAL(10,2) NOT NULL
);
CREATE TABLE IF NOT EXISTS "product" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "price" DECIMAL(10,2) NOT NULL,
    "image" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "order_product" (
    "order_id" UUID NOT NULL REFERENCES "order" ("id") ON DELETE CASCADE,
    "product_id" UUID NOT NULL REFERENCES "product" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
