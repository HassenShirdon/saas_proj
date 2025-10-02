import React, { useState } from "react";
import { Button } from "../ui/button";
import Logo from "@/assets/LogoIcon.svg";
import { Menu, X } from "lucide-react";
import { Link } from "react-router-dom";

const Header: React.FC = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const navigation = [
    { name: "Features", href: "#features" },
    { name: "Pricing", href: "#pricing" },
    { name: "Testimonials", href: "#testimonials" },
    { name: "About", href: "/About" },
  ];

  return (
    <header className="bg-white/80 backdrop-blur-md border-b border-gray-200/60 sticky top-0 z-50 supports-backdrop-blur:bg-white/60">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16 lg:h-20">
          {/* Logo */}
          <Link to="/" className="flex items-center space-x-3 group">
            <div className="w-10 h-10 lg:w-12 lg:h-12 rounded-lg transition-transform duration-200 group-hover:scale-105">
              <img
                src={Logo}
                alt="Marjaan Solutions"
                className="w-full h-full"
              />
            </div>
            <span className="text-xl lg:text-2xl font-bold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">
              Marjaan Solutions
            </span>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden lg:flex items-center space-x-8">
            {navigation.map((item) => (
              <a
                key={item.name}
                href={item.href}
                className="text-gray-600 hover:text-gray-900 transition-colors duration-200 font-medium relative group"
              >
                {item.name}
                <span className="absolute -bottom-1 left-0 w-0 h-0.5 bg-blue-600 transition-all duration-200 group-hover:w-full"></span>
              </a>
            ))}
          </nav>

          {/* Desktop CTA Buttons - FIXED: Remove asChild and use onClick */}
          <div className="hidden lg:flex items-center space-x-4">
            <Button
              variant="ghost"
              className="font-medium"
              onClick={() => (window.location.href = "/login")}
            >
              Sign In
            </Button>
            <Button
              className="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 font-medium shadow-lg shadow-blue-500/25 text-grey-50"
              onClick={() => (window.location.href = "/signup")}
            >
              Start Free Trial
            </Button>
          </div>

          {/* Mobile Menu Button */}
          <div className="lg:hidden">
            <Button
              variant="ghost"
              size="icon"
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="h-10 w-10"
            >
              {isMenuOpen ? (
                <X className="h-5 w-5" />
              ) : (
                <Menu className="h-5 w-5" />
              )}
            </Button>
          </div>
        </div>

        {/* Mobile Navigation - FIXED: Remove asChild */}
        {isMenuOpen && (
          <div className="lg:hidden animate-in slide-in-from-top-5 duration-200">
            <div className="px-2 pt-2 pb-4 space-y-1 bg-white/95 backdrop-blur-lg rounded-2xl border border-gray-200/60 mt-2 shadow-xl">
              {navigation.map((item) => (
                <a
                  key={item.name}
                  href={item.href}
                  className="block px-4 py-3 text-gray-700 hover:text-gray-900 hover:bg-gray-50 rounded-lg transition-colors duration-200 font-medium"
                  onClick={() => setIsMenuOpen(false)}
                >
                  {item.name}
                </a>
              ))}
              <div className="pt-2 border-t border-gray-200/60">
                <div className="flex flex-col space-y-2 px-4">
                  <Button
                    variant="ghost"
                    className="justify-start font-medium"
                    onClick={() => {
                      setIsMenuOpen(false);
                      window.location.href = "/login";
                    }}
                  >
                    Sign In
                  </Button>
                  <Button
                    className="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 font-medium justify-start"
                    onClick={() => {
                      setIsMenuOpen(false);
                      window.location.href = "/signup";
                    }}
                  >
                    Start Free Trial
                  </Button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </header>
  );
};

export default Header;
