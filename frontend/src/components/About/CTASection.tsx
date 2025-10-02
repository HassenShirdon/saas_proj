import React from "react";

const CTASection: React.FC = () => {
  return (
    <section className="py-16 bg-gradient-to-br from-blue-600 to-blue-700">
      <div className="container mx-auto px-6 max-w-6xl text-center">
        <h2 className="text-3xl font-bold text-white mb-4">
          Join Us on the Journey
        </h2>
        <p className="text-xl text-blue-100 mb-8 leading-relaxed">
          Marjaan Solutions is more than software—it's a partner in modernizing
          logistics operations in East Africa. Whether you're a small transport
          company or a large logistics firm, our platform is designed to make
          your daily work simpler, smarter, and more productive.
        </p>
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <button className="bg-white text-blue-600 hover:bg-gray-100 font-semibold py-3 px-8 rounded-lg transition-all duration-200">
            Get Started Today
          </button>
          <button className="border border-white text-white hover:bg-white/10 font-semibold py-3 px-8 rounded-lg transition-all duration-200">
            Contact Us
          </button>
        </div>
      </div>
    </section>
  );
};

export default CTASection;
