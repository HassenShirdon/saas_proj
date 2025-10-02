import React, { useState } from "react";
import clsx from "clsx";
import {
  ChevronDown,
  MessageCircle,
  Zap,
  Users,
  Shield,
  CreditCard,
} from "lucide-react";

const FAQSection: React.FC = () => {
  const [openItems, setOpenItems] = useState<Set<number>>(new Set());

  const toggleItem = (index: number) => {
    setOpenItems((prev) => {
      const newSet = new Set(prev);
      if (newSet.has(index)) {
        newSet.delete(index);
      } else {
        newSet.add(index);
      }
      return newSet;
    });
  };

  const faqs = [
    {
      id: 1,
      question: "How does the multi-tenant architecture benefit my business?",
      answer:
        "Our multi-tenant architecture ensures complete data isolation between different companies while maintaining a single, scalable infrastructure. This means each tenant gets their own secure workspace with custom configurations, user management, and data privacy, while we handle all the backend complexity and updates seamlessly.",
      icon: <Users className="h-5 w-5 text-blue-600" />,
      category: "Architecture",
    },
    {
      id: 2,
      question: "Can I customize the platform for my specific business needs?",
      answer:
        "Absolutely! We offer extensive customization options including custom workflows, role-based permissions, branded interfaces, and API integrations. Our platform is designed to adapt to various industries and business processes, with dedicated support for implementation and customization.",
      icon: <Zap className="h-5 w-5 text-green-600" />,
      category: "Customization",
    },
    {
      id: 3,
      question: "How secure is my data with Marjaan Solutions?",
      answer:
        "Security is our top priority. We employ enterprise-grade security measures including end-to-end encryption, SOC 2 compliance, regular security audits, and role-based access controls. Your data is stored in secure AWS data centers with 99.9% uptime SLA and comprehensive backup systems.",
      icon: <Shield className="h-5 w-5 text-purple-600" />,
      category: "Security",
    },
    {
      id: 4,
      question: "What happens after my 14-day free trial ends?",
      answer:
        "After your trial, you can choose from our flexible pricing plans that scale with your business. All your data and configurations are preserved during the transition. If you need more time to evaluate, you can request a trial extension or schedule a personalized demo with our solutions team.",
      icon: <CreditCard className="h-5 w-5 text-orange-600" />,
      category: "Billing",
    },
    {
      id: 5,
      question: "Do you offer onboarding and customer support?",
      answer:
        "Yes! We provide comprehensive onboarding including dedicated account setup, training sessions, and migration assistance. Our customer support includes 24/7 chat support, email support with 2-hour response time, and dedicated account managers for enterprise plans. We're committed to your success from day one.",
      icon: <MessageCircle className="h-5 w-5 text-teal-600" />,
      category: "Support",
    },
    {
      id: 6,
      question: "Can I integrate with other tools we're currently using?",
      answer:
        "Definitely. Our platform offers robust API endpoints and pre-built integrations with popular tools like Slack, QuickBooks, Salesforce, Google Workspace, and Microsoft 365. We also support custom webhook integrations and provide developer documentation for seamless connectivity with your existing tech stack.",
      icon: <Zap className="h-5 w-5 text-indigo-600" />,
      category: "Integrations",
    },
  ];

  return (
    <section
      id="faq"
      className="py-20 bg-gradient-to-br from-gray-50 to-indigo-50/20"
    >
      <div className="container max-w-6xl  mx-auto px-6">
        {/* Section Header */}
        <div className="text-center mb-16">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">
            Frequently Asked Questions
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Get answers to common questions about our platform, security, and
            how we can help transform your business operations.
          </p>
        </div>

        {/* FAQ Grid */}
        <div className="max-w-4xl mx-auto">
          <div className="space-y-4">
            {faqs.map((faq, index) => {
              const isOpen = openItems.has(index);

              return (
                <div
                  key={faq.id}
                  className={clsx(
                    "bg-white rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 border group",
                    isOpen ? "border-blue-200" : "border-gray-100"
                  )}
                >
                  <button
                    onClick={() => toggleItem(index)}
                    className="w-full flex items-start justify-between p-6 text-left hover:bg-gray-50/50 transition-colors duration-200"
                    aria-expanded={isOpen}
                  >
                    <div className="flex items-start space-x-4 flex-1">
                      <div className="flex-shrink-0 mt-1">
                        <div className="p-2 rounded-lg bg-gradient-to-br from-gray-50 to-gray-100 group-hover:scale-110 transition-transform duration-200">
                          {faq.icon}
                        </div>
                      </div>
                      <div className="flex-1">
                        <span className="text-xs font-semibold text-blue-700 bg-blue-50 px-2 py-1 rounded-full">
                          {faq.category}
                        </span>
                        <h3 className="text-lg font-semibold text-gray-900 mt-2 pr-4">
                          {faq.question}
                        </h3>
                      </div>
                    </div>
                    <div className="flex-shrink-0 ml-4 mt-1">
                      <ChevronDown
                        className={clsx(
                          "h-5 w-5 text-gray-400 transition-transform duration-300",
                          isOpen && "rotate-180"
                        )}
                      />
                    </div>
                  </button>

                  {/* Answer */}
                  {isOpen && (
                    <div className="px-6 pb-6 animate-in slide-in-from-top-5 duration-200">
                      <div className="pl-12 border-l-2 border-blue-200">
                        <p className="text-gray-600 leading-relaxed">
                          {faq.answer}
                        </p>
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>

          {/* Bottom CTA */}
          <div className="text-center mt-12">
            <div className="bg-gradient-to-r  from-blue-600 to-blue-700 rounded-2xl p-8 text-white">
              <h3 className="text-2xl font-bold mb-3">Still have questions?</h3>
              <p className="text-blue-100 mb-6 max-w-2xl mx-auto">
                Our team is here to help you get the answers you need and see
                how Marjaan Solutions can transform your business.
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <button className="bg-white text-blue-600 hover:bg-gray-100 font-semibold py-3 px-8 rounded-lg transition-all duration-200 shadow-lg hover:shadow-xl">
                  Contact Sales
                </button>
                <button className="border border-blue-400 text-white hover:bg-blue-600 font-semibold py-3 px-8 rounded-lg transition-all duration-200">
                  Schedule Demo
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default FAQSection;
