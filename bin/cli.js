#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");

// Skills to install (same as install.py)
const SKILLS = [
  "do",
  "product-requirements",
  "ask-questions-if-underspecified",
  "best-practices",
  "database-design",
  "backend-development",
  "frontend-design",
  "test-cases",
];

function expandHome(p) {
  if (p.startsWith("~/")) return path.join(require("os").homedir(), p.slice(2));
  return p;
}

function copyFileSync(src, dst) {
  fs.mkdirSync(path.dirname(dst), { recursive: true });
  fs.copyFileSync(src, dst);
  const stat = fs.statSync(src);
  fs.chmodSync(dst, stat.mode);
}

function copyDirRecursive(src, dst) {
  fs.mkdirSync(dst, { recursive: true });
  const entries = fs.readdirSync(src, { withFileTypes: true });

  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const dstPath = path.join(dst, entry.name);

    if (entry.isDirectory()) {
      copyDirRecursive(srcPath, dstPath);
    } else if (entry.isFile()) {
      copyFileSync(srcPath, dstPath);
    }
  }
}

function main() {
  const args = process.argv.slice(2);

  // Simple help
  if (args.includes("-h") || args.includes("--help")) {
    console.log("Usage: npx github:weihuacodeing11/myclaude");
    console.log("Installs myclaude skills to ~/.claude/");
    return;
  }

  const installDir = expandHome("~/.claude");
  const scriptDir = __dirname.endsWith("bin") ? path.dirname(__dirname) : __dirname;
  const skillsDir = path.join(installDir, "skills");

  console.log("Installing myclaude to ~/.claude/");

  // Create skills directory
  fs.mkdirSync(skillsDir, { recursive: true });

  // Copy each skill
  for (const skill of SKILLS) {
    const source = path.join(scriptDir, "skills", skill);
    const target = path.join(skillsDir, skill);

    if (!fs.existsSync(source)) {
      console.log(`  Warning: ${skill} not found in source`);
      continue;
    }

    if (fs.existsSync(target)) {
      console.log(`  Updating: ${skill}`);
      fs.rmSync(target, { recursive: true, force: true });
    } else {
      console.log(`  Installing: ${skill}`);
    }

    copyDirRecursive(source, target);
  }

  // Copy README.md and skill-rules.json
  for (const file of ["README.md", "skill-rules.json"]) {
    const source = path.join(scriptDir, "skills", file);
    const target = path.join(skillsDir, file);
    if (fs.existsSync(source)) {
      copyFileSync(source, target);
    }
  }

  console.log("\n✓ Installation complete!");
  console.log(`  Installed ${SKILLS.length} skills to: ${skillsDir}`);
  console.log("\nNext steps:");
  console.log('  1. Try: /do "build a todo app with user authentication"');
  console.log("  2. The workflow will guide you through 7 phases");
}

if (require.main === module) {
  try {
    main();
  } catch (err) {
    console.error("Error:", err.message);
    process.exit(1);
  }
}
