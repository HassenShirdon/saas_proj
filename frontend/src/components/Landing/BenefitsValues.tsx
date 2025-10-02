import React from "react";
import {
  CheckCircle,
  TrendingUp,
  Clock,
  Users,
  Shield,
  Zap,
} from "lucide-react";

const BenefitsSection: React.FC = () => {
  const benefits = [
    {
      icon: <TrendingUp className="h-8 w-8 text-blue-600" />,
      title: "Boost Operational Efficiency",
      description:
        "Automate repetitive tasks and streamline workflows to reduce manual work by up to 65%, allowing your team to focus on strategic initiatives.",
      metrics: "65% faster operations",
      color: "from-blue-500 to-blue-600",
    },
    {
      icon: <Clock className="h-8 w-8 text-green-600" />,
      title: "Save Valuable Time",
      description:
        "Cut reporting time from hours to minutes with automated data aggregation and real-time insights across all your business units.",
      metrics: "80% time savings",
      color: "from-green-500 to-green-600",
    },
    {
      icon: <Users className="h-8 w-8 text-purple-600" />,
      title: "Enhance Team Collaboration",
      description:
        "Break down departmental silos with unified platforms that enable seamless communication and data sharing across HR, finance, and operations.",
      metrics: "3x better collaboration",
      color: "from-purple-500 to-purple-600",
    },
    {
      icon: <Zap className="h-8 w-8 text-orange-600" />,
      title: "Accelerate Decision Making",
      description:
        "Access real-time analytics and predictive insights to make data-driven decisions faster, staying ahead of market trends and opportunities.",
      metrics: "2x faster decisions",
      color: "from-orange-500 to-orange-600",
    },
    {
      icon: <Shield className="h-8 w-8 text-indigo-600" />,
      title: "Ensure Compliance & Security",
      description:
        "Maintain full regulatory compliance with automated audits, role-based access controls, and enterprise-grade security protocols.",
      metrics: "100% compliance",
      color: "from-indigo-500 to-indigo-600",
    },
    {
      icon: <CheckCircle className="h-8 w-8 text-teal-600" />,
      title: "Drive Revenue Growth",
      description:
        "Identify new revenue opportunities and optimize resource allocation with intelligent forecasting and performance analytics.",
      metrics: "40% revenue increase",
      color: "from-teal-500 to-teal-600",
    },
  ];

  return (
    <section
      id="benefits"
      className="py-20 bg-gradient-to-br from-gray-50 to-blue-50/30"
    >
      <div className="container mx-auto px-6">
        {/* Section Header */}
        <div className="text-center mb-16">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">
            Transform Your Business Outcomes
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Beyond features—delivering measurable results that drive your
            business forward. Join thousands of companies achieving tangible
            success.
          </p>
        </div>

        {/* Benefits Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {benefits.map((benefit, index) => (
            <div
              key={index}
              className="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all duration-300 border border-gray-100 hover:border-blue-100 group"
            >
              {/* Icon with Gradient Background */}
              <div
                className={`inline-flex items-center justify-center p-3 rounded-2xl bg-gradient-to-r ${benefit.color} mb-6 group-hover:scale-110 transition-transform duration-300`}
              >
                {benefit.icon}
              </div>

              {/* Content */}
              <h3 className="text-xl font-semibold text-gray-900 mb-3">
                {benefit.title}
              </h3>

              <p className="text-gray-600 mb-4 leading-relaxed">
                {benefit.description}
              </p>

              {/* Metrics */}
              <div className="flex items-center justify-between">
                <span className="text-sm font-semibold text-gray-900 bg-gray-100 px-3 py-1 rounded-full">
                  {benefit.metrics}
                </span>
                <div className="w-8 h-0.5 bg-gradient-to-r from-gray-300 to-transparent"></div>
              </div>

              {/* Hover Effect Line */}
              <div className="w-0 h-0.5 bg-gradient-to-r from-blue-500 to-purple-500 mt-4 transition-all duration-300 group-hover:w-full"></div>
            </div>
          ))}
        </div>

        {/* Bottom CTA */}
        <div className="text-center mt-16">
          <div className="bg-white rounded-2xl p-8 shadow-lg border border-gray-100 max-w-4xl mx-auto">
            <h3 className="text-2xl font-bold text-gray-900 mb-4">
              Ready to See These Results in Your Business?
            </h3>
            <p className="text-gray-600 mb-6 max-w-2xl mx-auto">
              Join 5,000+ companies that have transformed their operations and
              achieved remarkable growth with our platform.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <button className="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white font-semibold py-3 px-8 rounded-lg transition-all duration-200 shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40">
                Start Free Trial
              </button>
              <button className="border border-gray-300 text-gray-700 hover:bg-gray-50 font-semibold py-3 px-8 rounded-lg transition-all duration-200">
                Schedule Demo
              </button>
            </div>
            <p className="text-sm text-gray-500 mt-4">
              No credit card required • 14-day free trial • Setup in minutes
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default BenefitsSection;
