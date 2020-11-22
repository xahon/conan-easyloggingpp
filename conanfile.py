import shutil
from conans import ConanFile, CMake


class EasyloggingppConan(ConanFile):
    name = "easyloggingpp"
    options = {
        "shared": [True, False]
    }
    default_options = {
        "shared": False
    }
    exports_sources = [
        "CMakeLists.txt"
    ]
    _source_subfolder = "src"

    def source(self):
        self.run("git clone git@github.com:amrayn/easyloggingpp.git --branch v%s --depth 1 %s" % (self.version, self._source_subfolder))
        shutil.copy("CMakeLists.txt", dst=self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self._source_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        if self.settings.os != "Linux":
            raise Exception("Not implemented")

        self.copy("*.h", src="%s/src/" % self._source_subfolder, dst="include")
        self.copy("*.a", dst="lib")
        self.copy("*.so", dst="lib")

    def package_info(self):
        self.cpp_info.libs = ["easyloggingpp"]