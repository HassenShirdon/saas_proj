import React from "react";
import { Star, Quote } from "lucide-react";

const TestimonialsSection: React.FC = () => {
  const testimonials = [
    {
      id: 1,
      name: "Sarah Chen",
      position: "CTO",
      company: "TechNova Solutions",
      image: "👩‍💼",
      rating: 5,
      text: "Marjaan Solutions transformed our multi-tenant management. We onboarded 15+ clients seamlessly with zero downtime. The role-based access and automation features saved us 40+ hours per week in manual operations.",
      stats: "65% faster client onboarding",
      color: "from-blue-500 to-blue-600",
    },
    {
      id: 2,
      name: "Marcus Rodriguez",
      position: "Operations Director",
      company: "Global Retail Corp",
      image: "👨‍💼",
      rating: 5,
      text: "The inventory and finance integration eliminated our data silos completely. Real-time reporting helped us reduce stockouts by 78% and improved cash flow visibility across all our locations.",
      stats: "78% reduction in stockouts",
      color: "from-green-500 to-green-600",
    },
    {
      id: 3,
      name: "Priya Patel",
      position: "HR Director",
      company: "GrowthScale Inc",
      image: "👩‍🎓",
      rating: 5,
      text: "Our HR processes became 3x more efficient. The automated payroll and attendance tracking reduced errors by 95%. Our team actually enjoys using the platform—that's rare for enterprise software!",
      stats: "95% reduction in payroll errors",
      color: "from-purple-500 to-purple-600",
    },
    {
      id: 4,
      name: "James Wilson",
      position: "CEO",
      company: "StartupScale Accelerator",
      image: "👨‍🚀",
      rating: 5,
      text: "As a startup working with multiple portfolio companies, the multi-tenant architecture is a game-changer. We manage 30+ companies in one platform while maintaining perfect data isolation and security.",
      stats: "30+ companies managed",
      color: "from-orange-500 to-orange-600",
    },
  ];

  return (
    <section
      id="testimonials"
      className="py-20 bg-gradient-to-br from-gray-900 to-blue-900"
    >
      <div className="container mx-auto px-6">
        {/* Section Header */}
        <div className="text-center mb-16">
          <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm rounded-full px-4 py-2 mb-6">
            <Star className="h-4 w-4 text-yellow-400 fill-current" />
            <span className="text-sm font-medium text-white">
              Rated 4.9/5 by 500+ companies
            </span>
          </div>
          <h2 className="text-4xl font-bold text-white mb-4">
            Trusted by Industry Leaders
          </h2>
          <p className="text-xl text-blue-200 max-w-3xl mx-auto">
            Don't just take our word for it. Here's what our customers have to
            say about transforming their operations with Marjaan Solutions.
          </p>
        </div>

        {/* Testimonials Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-7xl mx-auto">
          {testimonials.map((testimonial, index) => (
            <div key={testimonial.id} className="group relative">
              {/* Main Card */}
              <div className="relative bg-white rounded-2xl p-8 shadow-2xl hover:shadow-3xl transition-all duration-500 border border-white/20 backdrop-blur-sm h-full">
                {/* Quote Icon */}
                <div className="absolute -top-4 -left-4 w-12 h-12 bg-gradient-to-r from-blue-600 to-blue-700 rounded-2xl flex items-center justify-center shadow-lg">
                  <Quote className="h-6 w-6 text-white" />
                </div>

                {/* Rating */}
                <div className="flex items-center gap-1 mb-6">
                  {[...Array(testimonial.rating)].map((_, i) => (
                    <Star
                      key={i}
                      className="h-5 w-5 text-yellow-400 fill-current"
                    />
                  ))}
                </div>

                {/* Testimonial Text */}
                <blockquote className="text-gray-700 text-lg leading-relaxed mb-6 relative z-10">
                  "{testimonial.text}"
                </blockquote>

                {/* Stats Highlight */}
                <div className="inline-flex items-center gap-2 bg-gradient-to-r from-gray-50 to-blue-50 rounded-full px-4 py-2 mb-6">
                  <div
                    className={`w-2 h-2 bg-gradient-to-r ${testimonial.color} rounded-full`}
                  ></div>
                  <span className="text-sm font-semibold text-gray-900">
                    {testimonial.stats}
                  </span>
                </div>

                {/* Author Info */}
                <div className="flex items-center gap-4 pt-6 border-t border-gray-100">
                  <div className="flex items-center justify-center w-14 h-14 bg-gradient-to-br from-gray-100 to-gray-200 rounded-2xl text-2xl">
                    {testimonial.image}
                  </div>
                  <div className="flex-1">
                    <div className="font-semibold text-gray-900">
                      {testimonial.name}
                    </div>
                    <div className="text-sm text-gray-600">
                      {testimonial.position}
                    </div>
                    <div className="text-sm text-blue-600 font-medium">
                      {testimonial.company}
                    </div>
                  </div>
                </div>

                {/* Hover Gradient Effect */}
                <div
                  className={`absolute inset-0 bg-gradient-to-r ${testimonial.color} opacity-0 group-hover:opacity-5 rounded-2xl transition-opacity duration-500 pointer-events-none`}
                ></div>
              </div>

              {/* Floating Background Element */}
              <div
                className={`absolute -inset-4 bg-gradient-to-r ${testimonial.color} rounded-3xl opacity-0 group-hover:opacity-10 blur-xl transition-all duration-500 -z-10`}
              ></div>
            </div>
          ))}
        </div>

        {/* Trust Metrics */}
        <div className="mt-16 pt-12 border-t border-white/20">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 max-w-4xl mx-auto">
            {[
              { number: "500+", label: "Companies Trust Us" },
              { number: "99.9%", label: "Uptime SLA" },
              { number: "4.9/5", label: "Customer Rating" },
              { number: "24/7", label: "Support Coverage" },
            ].map((metric, index) => (
              <div key={index} className="text-center">
                <div className="text-3xl font-bold text-white mb-2">
                  {metric.number}
                </div>
                <div className="text-blue-200 text-sm font-medium">
                  {metric.label}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Bottom CTA */}
        <div className="text-center mt-12">
          <div className="bg-white/10 backdrop-blur-md rounded-2xl p-8 border border-white/20">
            <h3 className="text-2xl font-bold text-white mb-3">
              Ready to Join These Success Stories?
            </h3>
            <p className="text-blue-200 mb-6 max-w-2xl mx-auto">
              Start your journey today and experience the transformation that
              industry leaders trust.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <button className="bg-white text-blue-600 hover:bg-gray-100 font-semibold py-3 px-8 rounded-lg transition-all duration-200 shadow-lg hover:shadow-xl">
                Start Free Trial
              </button>
              <button className="border border-white text-white hover:bg-white/10 font-semibold py-3 px-8 rounded-lg transition-all duration-200">
                View Case Studies
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default TestimonialsSection;
