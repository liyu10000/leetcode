class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        int bitCount = 0;
        while (n > 0) {
            uint32_t b = n & 1;
            res = res << 1;
            res += b;
            n = n >> 1;
            bitCount++;
        }
        for (int i = 0; i < 32-bitCount; i++) {
            res = res << 1;
        }
        return res;
    }
};