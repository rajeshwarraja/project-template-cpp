from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout



class TemplateConanFile(ConanFile):
    name = "template"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    exports_sources = [ "lib/*", "host/*", "test/*", "CMakeLists.txt" ]


    def configure(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def requirements(self):
        self.test_requires("gtest/1.14.0")


    def layout(self):
        cmake_layout(self)


    def generate(self):
        tc = CMakeToolchain(self)
        tc.presets_prefix = "iconan"
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()
        cmake = CMake(self)
    
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        pass