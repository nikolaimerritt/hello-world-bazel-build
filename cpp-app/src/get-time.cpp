#include "get-time.h"
#include <ctime>

std::string get_time() {
  std::time_t result = std::time(nullptr);
  return std::string(std::asctime(std::localtime(&result)));
}
