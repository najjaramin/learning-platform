import LoginForm from "@/components/auth/LoginForm";
import Link from "next/link";

export default function LoginPage() {
  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      <div className="w-full max-w-md bg-white rounded-xl shadow-sm p-8">
        <h2 className="text-2xl font-bold text-center">
          Welcome back
        </h2>
        <p className="text-center text-gray-500 mt-1 mb-6">
          Login to your account
        </p>

        <LoginForm />

        <p className="text-center text-sm text-gray-500 mt-6">
          Don’t have an account?{" "}
          <Link href="/register" className="text-indigo-600">
            Sign up
          </Link>
        </p>
      </div>
    </div>
  );
}