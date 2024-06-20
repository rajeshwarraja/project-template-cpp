#include <lib.h>
#include <gtest/gtest.h>

TEST(LibraryTest, Hello) {
    ASSERT_STREQ("World!", lib::hello().c_str());
}
